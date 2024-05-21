# SNS y SQS
## Descripción del proyecto

Este proyecto proporciona scripts para publicar mensajes en un tema de SNS y 
recibir y procesar mensajes de una cola de SQS. Los scripts están escritos en Python y
utilizan la biblioteca boto3 para interactuar con los servicios de AWS.

### Requisitos

- Python 3.6 o superior
- Credenciales de acceso adecuadas 
- Acceso a una cuenta de AWS con un tema de SNS y una cola de SQS creados

### Instalación de dependencias
Clone el repositorio en su computadora local:

``` bash
git clone https://github.com/rduuqe/sqs_sns
```

Navegue hasta el directorio del proyecto:

``` bash
cd sqs_sns
```

Crea el entorno virtual:
Abre una terminal y navega hasta el directorio raíz de tu proyecto. Ejecuta el siguiente comando, reemplazando `mi_entorno` con el nombre deseado para tu entorno

```bash
python3 -m venv mi_entorno
```

Activa el entorno virtual:
Para activar el entorno virtual y comenzar a trabajar en tu proyecto, ejecuta el siguiente comando
``` bash
source mi_entorno/bin/activate
```

Instale las dependencias requeridas usando pip:
```
pip install -r requirements.txt
```

## Ejecución de scripts

### Publicar un mensaje en un tema de SNS

Ejecute el siguiente comando, reemplazando 
`Este es el mensaje` con el cuerpo del mensaje que desea publicar:

``` bash
/bin/bash publish_message.sh "Este es el mensaje"
```

### Recibir y procesar un mensaje de una cola de SQS

Ejecute el siguiente comando:

``` bash
/bin/bash ./receive_message.sh
```

## Explicación de los scripts

**publish_message.sh**: Este script ejecuta el script sns_publish.py para publicar un mensaje en un tema de SNS.

**receive_message.sh**: Este script ejecuta el script sqs_consumer.py para recibir y procesar un mensaje de una cola de SQS.

**sns_publish.py**: Este script publica un mensaje en un tema de SNS usando la biblioteca boto3.

**sqs_consumer.py**: Este script recibe un mensaje de una cola de SQS, procesa el cuerpo del mensaje y lo elimina de la cola

## Recursos adicionales

* [Documentación de Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)

* [Documentación de Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
    
* [Biblioteca boto3](https://aws.amazon.com/es/sdk-for-python/)

