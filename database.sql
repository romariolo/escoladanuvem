create database cadastro_clientes_prod;

use cadastro_clientes_prod;

create table clientes(

    id INT AUTO_INCREMENT PRIMARY kEY,
    nome VARCHAR(255),
    email VARCHAR(255),
    cep VARCHAR(8),
    endereco TEXT    

);