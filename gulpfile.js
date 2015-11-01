'use strict';

// requirements
var gulp = require('gulp');
var bourbon = require('node-bourbon');
var neat = require('node-neat');
var sass = require('gulp-sass');

// Run Sass on Default
gulp.task('default', ['sass']);

gulp.task('watch', function() {
    gulp.watch('blog/static/*.scss', ['sass']);
    gulp.watch('blog/static/**/*.scss', ['sass']);
});

gulp.task('sass', function () {
  gulp.src('blog/static/style.scss')
    .pipe(sass({
      // includePaths: require('node-bourbon').with('other/path', 'another/path')
      // - or -
      includePaths: require('node-bourbon').includePaths.concat(
        require('node-neat').includePaths)
    }))
    .pipe(gulp.dest('blog/static/'));
});
