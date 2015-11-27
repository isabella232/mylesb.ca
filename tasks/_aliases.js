module.exports = function (grunt) {
    'use strict';

    grunt.registerTask('develop', [
        'assemble:develop',
        'sass:deploy'
    ]);

    /*
      TODO Add some test/lint tasks here.
    */
    grunt.registerTask('test', []);

    /*
      TODO Add the S3 and rsync deploy tasks here.
    */
    grunt.registerTask('deploy', [
        'assemble:deploy',
        'sass:deploy'
    ]);

    grunt.registerTask('default', [
        'develop'
    ]);
};
