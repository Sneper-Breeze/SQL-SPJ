grammar sql;


query:   select  ';';

attribute : (table'.')var;

table : var;

join_condition : attribute EQ attribute;

condition : (attribute|var) comparison+ (attribute|var);

var : (WORD | NUM)+;

comparison : EQ|LT|GT;

join: 'JOIN' table (cross_product)* 'ON' join_condition;

cross_product: ',' table;

where: 'WHERE' condition ('AND' condition)*;

from: 'FROM' table (join|cross_product)* where?;

select: 'SELECT' ((ALL | attribute) ',')* (ALL | attribute) from;

ALL : '*';
EQ : '=';
LT : '<';
GT : '>';

WORD:   [A-Za-z]+ ;      // lower/uppercase identifiers
NUM :   [0-9]+;
WS  :   [ \t\r\n]+ -> skip ; // toss out whitespace
