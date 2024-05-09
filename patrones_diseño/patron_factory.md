# Factory Method

El patrón Factory es uno de los patrones fundamentales a nivel de diseño orientado a objeto. Este patrón pertenece al grupo de patrones creacionales y nos simplifica la construcción de una jerarquía de clases y las encapsula. Sin embargo a veces a la gente le cuesta ver como usar este patrón en su código. Vamos a utilizar un ejemplo sencillo en el que tendremos una jerarquía de clases Factura como se muestra a continuación.
-
<img src="https://www.arquitecturajava.com/wp-content/uploads/00119.gif"/>


Ya disponemos de las tres clases la clase abstracta y sus clases hijas. Como vemos la clase Factura es una clase abstracta de la cual heredan nuestras dos clases concretas que implementan el cálculo del IVA.  
-