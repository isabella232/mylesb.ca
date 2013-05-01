#!/usr/bin/env python

import os
from glob import glob

from fabric.api import env, puts, local, task, hosts
from fabric.contrib.project import rsync_project

from jinja2 import Environment, FileSystemLoader

env.hosts = ['nfs-myles-myles']
env.use_ssh_config = True
env.remote_path = '/home/public'
env.output_path = os.path.abspath('./_output')
env.site_path = os.path.abspath('./site')
env.template_path = os.path.abspath('./templates')
env.template_context = {
	'URL': 'http://mylesb.ca/'
}

def render(template, destination, **kwargs):
	jenv = Environment(loader=FileSystemLoader([env.template_path, env.site_path]))
	
	params = dict(env.template_context, **kwargs)
	params["PAGE"] = template
	
	text = jenv.get_template(template).render(params)
	
	with open(destination, "w") as output:
		puts("Rendering: {} to {}".format(template, destination))
		output.write(text.encode("utf-8"))

def render_site_html():
	for template in glob("%s/**.html" % env.site_path):
		filename = os.path.basename(template)
		render(filename, os.path.join(env.output_path, filename))

def clean():
	local("rm %s/*.html" % env.output_path)

@task(aliases=['build', 'build_html'], name="Build web site to HTML")
@hosts('localhost')
def build_html():
	clean()
	local("mkdir -p %s" % env.output_path)
	render_site_html()

@task(name="Deploy web site.")
@hosts('nfs-myles-myles')
def deploy():
	build_html()
	
	rsync_project(
		local_dir=env.output_path,
		remote_dir=env.remote_path,
		delete=True,
		extra_opts='--exclude=".DS_Store"'
	)