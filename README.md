Trabajo Final - Criptografía Aplicada 
Autor: Sebastián Emilio Mayo 
Asignatura: Criptografía Aplicada 
Contenido: Resolución de desafíos seleccionados y material reproducible. Este Incluye código para ejecutar en local o Colab, explicaciones y recomendaciones de mitigación. 
  
Índice 
1.	Introducción general 
2.	Desafío 1 — Clave generada a partir de fecha y hora (Aleatoriedad) 
3.	Desafío 2 — Secuencia cifrante repetida (Cifrado de flujo) 
4.	Desafío 3 — Cambio de bits en modo CBC (Cifrado de bloques) 
5.	Herramientas y cómo ejecutar los scripts 
6.	Conclusiones generales 
7.	Anexos (código fuente y archivos ejemplo) 
  
1. Introducción general 
En este trabajo se resuelven y analizan tres desafíos representativos de debilidades criptográficas: malas fuentes de entropía, reuso de keystream en cifrados de flujo y manipulación de mensajes cifrados en modo CBC mediante flips de bits. Para cada desafío se incluye: 
•	Descripción mínima del desafío 
•	Análisis del problema y razones técnicas 
•	Desarrollo de la solución con código reproducible 
•	Prevención / formas de evitar el problema 
•	Herramientas y referencias 
  
