## Vantagem e desenvolvimento de web services

É uma solução utilizada para haver intregração e comunicação entre aplicações diferentes, por meio de uma linguagem de programação, independente da linguagem utilizada.

Referências: 
[Web Services](https://pt.wikipedia.org/wiki/Web_service)
[Web service: o que é, como funciona, para que serve?](https://www.opensoft.pt/web-service/)
#### SOAP
*Simple Object Acces Proocol*ou Protocolo Simples de Acesso ao Objeto é um protocolo baseado em XML (*Extensible Markup Language*) que permite a troca de informações usando o protocolo HTTP,  identificado por URI (*Uniform Resource Identifier*). 
##### Exemplo:
Existem uma aplicação X e outra aplicação Y criado com bancos de dados e linguagens diferentes. Para que essas comunicações possam se comunicar um ao outro (a aplicação Y ter acesso ao banco de dado de aplicação X), a aplicação Y deve expor uma URI através de linguagem demarcaçao XML ou Json, por exemplo, e protocolo HTTP para Web Service., realizando uma requisição. Em seguida,  esta requisição será feita a consulta no banco de dado X, devovendo informações ao Y.
