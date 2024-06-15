grammar sql;


query:   select  ';';

attribute : (table'.')?var;

table : var;

join_condition : attribute EQ attribute;

condition : (attribute|NUM) comparison (attribute|NUM);

var : (WORD | NUM)+;

comparison : EQ|NE|LT|LE|GT|GE;

join: 'JOIN' table 'ON' join_condition;

where: 'WHERE' condition;

select: 'SELECT' ((ALL | attribute) ',')* (ALL | attribute) from;

from: 'FROM' table join* where*;

ALL : '*';
EQ : '=';
NE : '!=';
LT : '<';
LE : '<=';
GT : '>';
GE : '>=';

WORD:   [A-Za-z]+ ;      // lower/uppercase identifiers
NUM :   [0-9]+;
WS  :   [ \t\r\n]+ -> skip ; // toss out whitespace
