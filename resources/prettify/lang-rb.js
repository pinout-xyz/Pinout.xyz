/**
 * @fileoverview
 * Registers a language handler for Ruby.
 * When in doubt, this module attempts to mimic vim. 
 * Ruby grammar: http://www.cse.buffalo.edu/~regan/cse305/RubyBNF.pdf
 *
 * @author matthew.y.king@gmail.com
 */

PR.registerLangHandler(PR.createSimpleLexer([
  // # comment
  [PR['PR_COMMENT'], /^#[^\r\n]*/, null, '#']
  // 'foo', "foo", `foo`
  // String interpolation is unsupported.
, [PR['PR_STRING'], /^([\'\"\`])(?:(?!\1)|[^\\]|\\[\s\S])*?(?:\1|$)/, null, '\'\"\`']
], [
  // =begin
  // comment
  // =end
  // `=begin` must be located at the beginning of the line.
  // At this time, the case where `=begin` begins a source file is not accounted for.
  [PR['PR_COMMENT'], /^[\r\n]=begin\b[\s\S]*?(?:=end|$)/]
  // %q{}, %q[], %q(), %q<> (balanced quotes)
  // Nested balanced quotes are unsupported.
, [PR['PR_STRING'], /^%[qQ](?:\{(?:[^\}\\]|\\[\s\S])*?(?:\}|$)|\[(?:[^\]\\]|\\[\s\S])*?(?:\]|$)|\((?:[^\)\\]|\\[\s\S])*?(?:\)|$)|\<(?:[^\>\\]|\\[\s\S])*?(?:\>|$))/]
  // %q||, etc (generic non-balanced quotes)
, [PR['PR_STRING'], /^%[qQ](.)(?:(?!\1)|[^\\]|\\[\s\S])*?(?:\1|$)/]
  // <<HEREDOC
, [PR['PR_STRING'], /^<<(\w+)[\s\S]*?[\r\n]\1/]
  // <<'HEREDOC'
  // For quoted heredocs, ruby requires `'` or `"` quotes, and ruby does not allow escaped quotes or line breaks.
, [PR['PR_STRING'], /^<<(?=[\'\"]([ \w]+)[\'\"])(?:\'\1\'|\"\1\")[\s\S]*?[\r\n]\1/]
  // <<-HEREDOC
, [PR['PR_STRING'], /^<<-(\w+)[\s\S]*?\1/]
  // <<-'HEREDOC'
, [PR['PR_STRING'], /^<<-(?=[\'\"]([ \w]+)[\'\"])(?:\'\1\'|\"\1\")[\s\S]*?\1/]
  // /regex/options
, ['lang-regex', /^(?:^^\.?|[+-]|[!=]=?=?|\#|%=?|&&?=?|\(|\*=?|[+\-]=|->|\/=?|::?|<<?=?|>>?>?=?|,|;|\?|@|\[|~|{|\^\^?=?|\|\|?=?|break|case|continue|delete|do|else|finally|instanceof|return|throw|try|typeof|when)\s*(\/(?:[^\/\\]|\\[\s\S])+?(?:\/|$)[a-z]*)/]
  // %r{}, %r[], %r{}, %r<> (balanced delimiters)
, [PR['PR_STRING'], /^%r(?:\{(?:[^\}\\]|\\[\s\S])*?(?:\}|$)|\[(?:[^\]\\]|\\[\s\S])*?(?:\]|$)|\((?:[^\)\\]|\\[\s\S])*?(?:\)|$)|\<(?:[^\>\\]|\\[\s\S])*?(?:\>|$))[a-z]*/]
  // %r||, etc (generic non-balanced delimiters)
, [PR['PR_STRING'], /^%r(.)(?:(?!\1)|[^\\]|\\[\s\S])*?(?:\1|$)[a-z]*/]
  // :symbol, :'symbol', symbol:
, [PR['PR_LITERAL'], /^(?::[\w\?!]+|:([\'\"\`])(?:(?!\1)|[^\\]|\\[\s\S])*?(?:\1|$)|[\w\?!]+:(?!:))/]
  // Exclude `::` (as in Foo::method)
, [PR['PR_PLAIN'], /^::/]
  // ?a (the character 'a')
, [PR['PR_LITERAL'], /^(?:\?.)\b/]
  // Exclude `method?`
, [PR['PR_PLAIN'], /^\w\?/]
  // 0b01, 0x1aA, 1.2e12
  // Accept `_` within numbers.
, [PR['PR_LITERAL'], /^\b(?:0b[_01]+|0x[_a-f0-9]+|\d+[_\d]*\.?(?:\d[_\d]*)?(?:e[+\-]?\d[_\d]*)?)\b/i]
  // Exclude `method1`
, [PR['PR_PLAIN'], /^\w\d+/]
  // scope variables (@foo, @@foo, $foo), capitalized types, CONSTANTs, built-in dollar variables
, [PR['PR_TYPE'], /^(?:(?:@|@@|\$)\w+|[A-Z]+[a-z]\w+|[A-Z][_A-Z0-9]*)\b|\$./]
  // keywords
, [PR['PR_KEYWORD'], /^\b(?:BEGIN|END|alias|and|begin|break|case|class|def|do|else|elsif|end|ensure|extend|false|for|if|lambda|in|include|module|next|nil|not|or|private|proc|protected|redo|require|rescue|retry|return|self|super|true|undef|unless|until|when|while|yield)\b/]
]), ['rb']);