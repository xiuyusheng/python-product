const JSEncrypt=require('node-jsencrypt')
var aa=function(PUBLIC){
var encrypt = new JSEncrypt();
encrypt.setPublicKey(PUBLIC);
return (encrypt.encrypt('20030216abc'));
}
