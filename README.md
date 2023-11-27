# Data Compliance


![Data-Compliance](images\data-compliance.jpg)

La importancia del cumplimiento normativo de datos, también conocido como data compliance, en las empresas es fundamental en el panorama actual, donde la información se ha convertido en uno de los activos más valiosos. El data compliance se refiere al conjunto de prácticas y medidas que una organización adopta para garantizar que la recopilación, almacenamiento, procesamiento y transmisión de datos cumplan con las leyes y regulaciones aplicables.

En un mundo cada vez más digitalizado, las empresas manejan grandes cantidades de información personal y confidencial de clientes, empleados y socios comerciales. El incumplimiento de las normativas de protección de datos puede tener consecuencias graves, tanto a nivel legal como reputacional. Las sanciones por violaciones a la privacidad y la seguridad de los datos pueden resultar en multas significativas y pérdida de confianza por parte de los clientes y otras partes interesadas.

El data compliance no solo se trata de cumplir con requisitos legales, sino también de construir una base sólida para la confianza del cliente. Las empresas que demuestran un compromiso serio con la protección de la información ganan la confianza de sus clientes y pueden diferenciarse positivamente en un mercado cada vez más competitivo. Además, el cumplimiento normativo contribuye a la gestión eficiente de riesgos, ya que ayuda a prevenir la pérdida de datos, el robo de identidad y otros incidentes de seguridad que podrían perjudicar la estabilidad operativa de la empresa.


# Contenido del proyecto

- **get_data.py** : Este script cumple la función de extraer información de diversas fuentes de datos. No solo se encarga de la recolección de datos, sino que también realiza procesos de transformación para estructurar la información de manera adecuada. Finalmente, almacena los datos procesados en archivos CSV y XLSX, proporcionando así una base de datos organizada y lista para su posterior análisis.


- **EDA.ipynb**: En este Notebook se realiza un examen detallado de los datos recopilados. Aquí se llevó a cabo el análisis exploratorio de datos y se formularon respuestas a preguntas mediante gráficos.


# ¿Que es el GDPR?

El Reglamento General de Protección de Datos (GDPR, por sus siglas en inglés) es una regulación de la Unión Europea que entró en vigencia el 25 de mayo de 2018. Su objetivo principal es fortalecer y unificar las normativas de protección de datos para todos los individuos dentro de la Unión Europea (UE) y del Espacio Económico Europeo (EEE).

Con el propósito de proporcionar información actualizada sobre las multas impuestas a personas físicas y jurídicas que forman parte de la Unión Europea, el GDPR ofrece un seguimiento detallado a través del sitio web **https://www.enforcementtracker.com/**. Para llevar a cabo el análisis correspondiente, se extrajo información directamente de esta plataforma web.


# ¿Que es la ley 25.326?

La Ley N.º 25.326 de Argentina, conocida como la "Ley de Protección de Datos Personales" o "Ley de Habeas Data", fue sancionada el 4 de octubre de 2000 y regula la protección integral de los datos personales asentados en archivos, registros, bancos de datos, u otros medios técnicos de tratamiento de datos, sean estos públicos o privados.

Esta legislación reconoce los derechos de los titulares de datos personales, los cuales comprenden el acceso, rectificación, actualización, inclusión o supresión de los datos cuando estos resulten incorrectos o incompletos. Asimismo, establece que los datos personales deben ser tratados con una finalidad específica y legítima, asegurando que sean adecuados, pertinentes y no excesivos en relación con la finalidad para la cual fueron recopilados, entre otras disposiciones.

Para llevar a cabo el análisis correspondiente a esta ley, se empleó información obtenida del buscador de normativa vigente de la Agencia de Acceso a la Información Pública, disponible en **https://www.argentina.gob.ar/aaip/buscador-normativa.**




# Distribución de Multas en Países según el Recuento y Monto Total

![imagen_1](images\sanciones-por-pais.png)

![Imagen_2](images\acumulacion-de-multas-por-pais.png)

En este gráfico se pueden observar los 10 países que recibieron más multas. El primer punto que destaca es que España acumula la mayor cantidad de multas, llegando casi a 800, lo que representa más del doble que su seguidor más cercano. Sin embargo, cuando se realiza una agrupación por el monto total de la multa aplicada, encontramos que Irlanda encabeza la lista, al mismo tiempo que no es uno de los países que más multas individuales ha obtenido.

Este comportamiento lo atribuimos a varios factores que se hacen evidentes al observar cuáles son los tipos de empresas que reciben multas en estos países.

---

![Imagen_3](images\Industrias-españolas-multadas.png)
![Imagen_4](images\Industrias-irlandesas-multadas.png)

La media de las sanciones aplicadas en España no excede los 100.000 euros y, por norma general, se imponen debido a que la empresa en cuestión no tiene las bases legales para procesar los datos que ha recogido. 

Por otra parte, en Irlanda, la tasa impositiva en el impuesto de sociedades es del 12.5%, la más baja de la Unión Europea. Esto no es un dato menor, ya que, como veremos más adelante, Irlanda es el asiento principal de las mayores empresas de redes sociales en el continente europeo, **particularmente de Meta**.

[Carga Impositiva en Irlanda](https://expansion.mx/tecnologia/2021/06/28/por-que-irlanda-es-tan-importante-para-las-tecnologicas)

[Multas en España](https://www.eleconomista.es/tecnologia/noticias/12325618/06/23/espana-sigue-siendo-el-pais-que-mas-multas-recibe-por-infracciones-del-rgpd-.html)


# Articulos en los que mas se sustentaron las sanciones

El Reglamento General de Protección de Datos (GDPR) establece principios fundamentales y medidas para garantizar la protección de datos personales. Según **el Artículo 5,** se enfatiza la legalidad, equidad y transparencia en el procesamiento, así como la limitación de la finalidad, minimización de datos, exactitud, almacenamiento limitado y la aplicación de medidas de integridad y confidencialidad.

**El Artículo 6** del GDPR detalla las bases legales para el procesamiento de datos, incluyendo el consentimiento, ejecución de contratos, cumplimiento de obligaciones legales, protección de intereses vitales, tareas de interés público y el ejercicio de poderes oficiales, así como la legitimidad de intereses perseguidos por el responsable del tratamiento.

Por otro lado, **el Artículo 32** establece medidas de seguridad que las organizaciones deben adoptar para proteger los datos personales. Esto incluye la seguridad del tratamiento, la evaluación del riesgo, la pseudonimización y cifrado, la garantía de confidencialidad, integridad, disponibilidad y resiliencia de los sistemas, la restauración eficiente de la disponibilidad de datos, así como la verificación y evaluación regulares, y la formalización por escrito de acuerdos con encargados del tratamiento. En conjunto, estos elementos buscan asegurar un procesamiento de datos seguro y conforme a los principios del GDPR.

![Imagen_5](images\normativa-mas-afectada.png)


Se observa que la mayoría de las multas se concentran en violaciones a los principios fundamentales protegidos por el GDPR, el incumplimiento de las obligaciones de las empresas al proteger los datos y las fallas al obtenerlos y procesarlos. 

![Imagen_6](images\multas.png)

Cuando analizamos las multas más cuantiosas impuestas, observamos que estas se fundamentan en varios artículos del GDPR. No obstante, llama la atención un valor atípico: la sanción más elevada tiene su base en el Artículo 46, inciso 1, del GDPR, el cual trata sobre las transferencias de datos personales a terceros países u organizaciones internacionales. A continuación, se presenta un resumen de dicho artículo:

>**Artículo 46 (1) - Transferencias sujetas a garantías adecuadas:**
>
>*Principio General:*
>Las transferencias de datos personales a terceros países u organizaciones internacionales solo son permitidas si el responsable del tratamiento o el encargado del >tratamiento ha proporcionado garantías adecuadas para la protección de datos personales.
>
>*Tipos de Garantías:*
>Las garantías adecuadas pueden lograrse mediante cláusulas contractuales tipo aprobadas por la Comisión Europea o mediante instrumentos vinculantes de corporativos. También >puede considerarse otras formas de garantías, como decisiones de adecuación adoptadas por la Comisión Europea.
>
>*Proceso de Aprobación:*
>Las cláusulas contractuales tipo y los instrumentos vinculantes de corporativos deben ser aprobados por la autoridad de control competente, en consulta con el Comité >Europeo de Protección de Datos.
>
>*Derechos Ejecutables y Recursos Jurídicos:*
>Las cláusulas contractuales tipo y los instrumentos vinculantes de corporativos deben contener disposiciones que permitan a los interesados ejercer derechos ejecutables y >tener recursos jurídicos efectivos.

En este caso, Meta fue sancionada por violar la privacidad de sus usuarios y por la presunta triangulación de información con el gobierno de los Estados Unidos.

Si comparamos el monto de esta única sanción con el resto, observamos lo desorbitante de la multa. Aunque un posible motivo de esta sanción podría ser el carácter ejemplificativo que se le atribuye, dado que estos casos prácticamente carecen de precedentes. Es posible que se esté buscando establecer jurisprudencia sobre el caso en cuestión.

![Imagen_7](images\montos-de-normativa.png)

[Link a nota sobre el caso](https://www.forbes.com.mx/irlanda-multa-meta-1200-millones-infringir-normativa-privacidad-datos/)


# Industrias más Sancionadas

![Imagen_8](images\multas-por-actividad.png)

![Imagen_9](images\sanciones-por-actividad.png)

Aunque a estas altura se podría llegar a predecir cual es la indutria mas sancionada, siendo estas la que compone telecomunicaciones, media y broadcasting, cuando la medicion es por la cuantia de la multa, no es menor el recuento que se encuentra en 










