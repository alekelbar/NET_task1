#include <iostream>
int main()
{
  int i = 0, j = 0, d[] = {3, 5, 2};
  std::string b = "";
  char c;
  FILE *fichero;
  fichero = fopen("./data/decode.bin", "rb");
  while (!feof(fichero))
  {
    c = fgetc(fichero);
    if (c >= 65 && c <= 90)
    {
      c -= d[j];
      if (c < 65)
        c = c - 64 + 90;
    }
    else if (c == 126)
      c = 32;
    b += c;
    i++;
    if (j < 2)
      j++;
    else
      j = 0;
  }
  fclose(fichero);
  std::cout << "CADENA DECODIFICADA: " << b << std::endl;
  std::cout << "FIN DEL PROGRAMA" << std::endl;
  return 0;
}