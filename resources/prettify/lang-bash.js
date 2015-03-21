/**
 * @fileoverview
 * Registers a language handler for Ruby.
 * When in doubt, this module attempts to mimic vim. 
 * Ruby grammar: http://www.cse.buffalo.edu/~regan/cse305/RubyBNF.pdf
 *
 * @author matthew.y.king@gmail.com
 */

PR.registerLangHandler(PR.createSimpleLexer([], [ 



['fun', /^\b(?:sudo)\b/],

[PR['PR_KEYWORD'], /^\b(?:grep|awk|apt-get|chkconfig|vi|modprobe)\b/]


]), ['bash']);