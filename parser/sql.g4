grammar sql;


query:   select  ';';

attribute : (table'.')var;

table : var;

join_condition : attribute EQ attribute;

condition : (attribute|var) comparison+ (attribute|var);

var : (WORD | NUM)+;

comparison : EQ|LT|GT;

join: 'JOIN' table 'ON' join_condition;

where: 'WHERE' condition ('AND' condition)*;

select: 'SELECT' ((ALL | attribute) ',')* (ALL | attribute) from;

from: 'FROM' table join* where?;

ALL : '*';
EQ : '=';
LT : '<';
GT : '>';

WORD:   [A-Za-z]+ ;      // lower/uppercase identifiers
NUM :   [0-9]+;
WS  :   [ \t\r\n]+ -> skip ; // toss out whitespace
