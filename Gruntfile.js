module.exports = function (grunt) {
    'use strict';

    grunt.initConfig({
        aws: grunt.file.readJSON('.aws.json'),
        pkg: grunt.file.readJSON('package.json'),
        config: grunt.file.readYAML('config.yaml')
    });

    require('matchdep').filterDev('grunt-*').forEach(grunt.loadNpmTasks);

    grunt.task.loadTasks('./tasks/');
};
