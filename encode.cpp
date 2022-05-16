#include <iostream>
#include <fstream>
#include <fstream>

int main()
{
  int i = 0, j = 0, d[] = {3, 5, 2};
  std::string b = "";
  char c;
  FILE *fichero;
  fichero = fopen("./data/encode.bin", "rb");
  while (!feof(fichero))
  {
    c = fgetc(fichero);
    // Codificar ...
    if (c >= 65 && c <= 90)
    {
      c += d[j];
      if (c > 90)
        c = c - 90 + 64;
    }
    else if (c == 32)
      c = 126;
    // Codificar ...
    b += c;
    i++;
    if (j < 2)
      j++;
    else
      j = 0;
  }
  fclose(fichero);

  // Escribir la codificación ...
  std::ofstream f("./data/decode.bin");
  if (f.is_open())
    f << b << std::endl;
  else
    std::cerr << "Error de apertura del archivo." << std::endl;

  std::cout
      << "Resultado: " << b << std::endl;
  std::cout << "FIN DEL PROGRAMA" << std::endl;
  return 0;
}