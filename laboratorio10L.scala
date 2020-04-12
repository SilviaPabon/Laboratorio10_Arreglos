

object laboratorio10L {

  def main(args: Array[String]) {
    print("Ingresar el número a calcular: ")
    var n = scala.io.StdIn.
      readInt()
    var sumador = 0: Int
    var a = 0: Int

    for (i <- 1 to n-1) {
      if (n % i == 0) {
        sumador += i
      }
    }
        if (sumador == n) {
          println("El número es perfecto, sus divisores suman:" + sumador)
        }
        else{
          println("El número no es perfecto, sus divisores suman:" + sumador)
        }
  }
}
