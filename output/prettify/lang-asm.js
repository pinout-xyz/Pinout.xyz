var a=null;
PR.registerLangHandler(PR.createSimpleLexer(
[
["com",/^@[^\n\r]*/,a,"@"],
["pln",/^[\t\n\r \xa0]+/,a,"\t\n\r \xa0"],
["str",/^"(?:[^"\\]|\\[\S\s])*(?:"|$)/,a,'"']
],
[
["typ",/^(?:\.ascii|\.long)\b/,a],
["cls",/^(?:\.data|\.text|\.globl|\.code)\b/,a],
["fun",/^b(eq|le)?[\ \t]*(?:[A-Za-z_]*)\b/,a],
["kwd",/^(?:mov|ldr|svc|cmp|beq|add|ble|b|LSL|LSR)\b/,a],
["cls",/^r\d/],
["fun",/^[A-Za-z_]*:/],
["fun",/^\=[A-Za-z_]*\b/],
["arg",/^\#\dx[\d]+/]
]
),["asm"]
);
