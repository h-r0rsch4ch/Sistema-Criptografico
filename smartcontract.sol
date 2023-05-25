// SPDX-License-Identifier: MIT
pragma solidity 0.8.18;

contract registros{
    address public persona;

    //Crear el cosntructor
    constructor(){
        persona = msg.sender;
    }

    //Mapping para relacionar los hash con los datos de la persona
    mapping (bytes32=>string) Registrosnombre;

    //Evento
    event registrocertificado(bytes32, string);

    //Funcion para registrar las personas 
    function RegistrarPersonas(string memory _idpersona, string memory _nombrepersona)public{
        //hash de la persona 
        bytes32 hash_idpersona= keccak256(abi.encodePacked(_idpersona));
        //Relacionar el hash de las personas con sus datos
        Registrosnombre[hash_idpersona] = _nombrepersona;

        emit registrocertificado(hash_idpersona, _nombrepersona);
    }
    //Funcion para ver registros 
    function VerRegistros(string memory _idpersona)public view returns(bytes32, string memory){
        //hash de la persona
        bytes32 hash_idpersona= keccak256(abi.encodePacked(_idpersona));
        //Indicadores de la persona
        string memory nombrePersona = Registrosnombre[hash_idpersona];

        return(hash_idpersona, nombrePersona);
    }
}
