# GFD-Wave
Generalized Finite Differences Methods for numerically solve Wave Equation on highly irregular regions.

All the codes are distributed under MIT License on [GitHub](https://github.com/gstinoco/GFD-Wave) and are free to use, modify, and distribute giving the proper copyright notice.

![Approximate and Theoretical solutions of the problem on ZIR region](/Results/Clouds/Explicit/Steps/ZIR_2_05.png)

## Description :memo:
This repository proposes a way to make an approximation to Wave Equation in two dimensions over regions that can range from regular (CUA) to highly irregular (ENG).

For this, the proposed solution uses a Generalized Finite Differences Method for the numerical solution over all the regions on:<br>
1. Triangulations.
2. Unstructured clouds of points.

Zirahuen Structured Grid                                      | Zirahuen Triangulation
:------------------------------------------------------------:|:------------------------------------------------------------:
![Zirahuen Lake Region](/Data/Meshes/ZIR_2.png)               | ![Zirahuen Lake Triangulation](/Data/Clouds/ZIR_2_Tri.png)
Zirahuen Cloud of Points                                      | Zirahuen Cloud of Points With Holes
![Zirahuen Lake Cloud of Points](/Data/Clouds/ZIR_2.png)      | ![Zirahuen Lake Cloud of Points](/Data/Holes/ZIR_2.png)


It is possible to find all test data in the "Data" folder and some sample results in the "Results" folder.

## Researchers :scientist:
All the codes presented were developed by:
    
  - Dr. Gerardo Tinoco Guerrero<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    Aula CIMNE-Morelia<br>
    gerardo.tinoco@umich.mx<br>
    https://orcid.org/0000-0003-3119-770X

  - Dr. Francisco Javier Domínguez Mota<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    Aula CIMNE-Morelia<br>
    francisco.mota@umich.mx<br>
    https://orcid.org/0000-0001-6837-172X
  
  - Dr. José Gerardo Tinoco Ruiz<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    jose.gerardo.tinoco@umich.mx<br>
    https://orcid.org/0000-0002-0866-4798

  - Dr. José Alberto Guzmán Torres<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    Aula CIMNE-Morelia<br>
    jose.alberto.guzman@umich.mx<br>
    https://orcid.org/0000-0002-9309-9390

## Students :man_student: :woman_student:
  - Heriberto Arias Rojas<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    heriberto.arias@umich.mx<br>
    https://orcid.org/0000-0002-7641-8310

  - Ricardo Román Gutiérrez<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    ricardo.roman@umich.mx<br>
    https://orcid.org/0000-0001-8521-9391

## Funding :dollar:
With the financing of:

  - National Council of Science and Technology, CONACyT (Consejo Nacional de Ciencia y Tecnología, CONACyT), México.
  
  - Coordination of Scientific Research, CIC-UMSNH (Coordinación de la Investigación Científica de la Universidad Michoacana de San Nicolás de Hidalgo, CIC-UMSNH), México.
  
  - Aula CIMNE-Morelia, México.