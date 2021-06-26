/*
    Implement the supersampling technique on the triangle drawn using bounding box algorithm.
*/



#include <GL/glut.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include<iostream>

using namespace std;

void init (void)
{
	glClearColor (1.0, 1.0, 1.0, 0.0);
	glMatrixMode (GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D (-100.0, 650.0, -100.0, 650.0);
}

int findmin(int a , int b, int c) {
	a = min(a, b);
	return min(a, c);
}

int findmax(int a , int b, int c) {
	a = max(a, b);
	return max(a, c);
}

void TriangleRaster (void)
{
	glClear (GL_COLOR_BUFFER_BIT);
	glColor3f (0.0, 0.4, 0.2);


	int x0 = 50 * 4 , x1 = 0 * 4 , x2 = 150 * 4;
	int y0 = 150 * 4 , y1 = 0 * 4 , y2 = 0 * 4;

	int dx0 = x1 - x0 , dx1 = x2 - x1 , dx2 = x0 - x2;
	int dy0 = y1 - y0 , dy1 = y2 - y1 , dy2 = y0 - y2;

	int x_min = findmin(x0 , x1 , x2);
	int y_min = findmin(y0 , y1 , y2);

	int x_max = findmax(x0 , x1 , x2);
	int y_max = findmax(y0 , y1 , y2);


	int q = x_max - x_min;

	int f0 = (x_min - x0) * dy0 - (y_max - y0) * dx0;
	int f1 = (x_min - x1) * dy1 - (y_max - y1) * dx1;
	int f2 = (x_min - x2) * dy2 - (y_max - y2) * dx2;

	int buffer[752][752] = {0};


	// Creating Buffer to store pixel information of the complete window.
	// For ease of calculation we padded with zeros

	glBegin (GL_POINTS);

	for (int i = y_max; i >= y_min; i--) {
		for (int j = x_min; j <= x_max; j++) {

			if ((f0 < 0) and (f1 < 0) and (f2 < 0)) {

				buffer[j][i] = 1;

			}

			f0 = f0 + dy0;
			f1 = f1 + dy1;
			f2 = f2 + dy2;

		}

		f0 = f0 - q * dy0;
		f0 = f0 + dx0;

		f1 = f1 - q * dy1;
		f1 = f1 + dx1;

		f2 = f2 - q * dy2;
		f2 = f2 + dx2;
	}

	// Convolving with mask of size 4x4 , which will replace the 4x4 window to the average of the 4x4 window
	// i.e converting 4X resolution image to 1X resolution.
	// Storing resultant in result array.

	float result[188][188] = {0.0};

	for (int i = 0; i < 188; i++) {
		for (int j = 0; j < 188; j++) {

			float temp = 0;
			for (int k = 4 * i; k < 4 + 4 * i; k++) {

				for (int p = 4 * j; p < 4 + 4 * j; p++) {

					temp += buffer[k][p];

				}

			}

			result[i][j] = temp / 16;

		}

	}

	//Displaying the window after supersampling.

	for (int i = 0; i < 188; i++) {
		for (int j = 0; j < 188; j++) {

			if (result[i][j] != 0 ) {

				GLint a = i, b = j;
				glVertex2i(a, b);

			}
		}
	}


	glEnd ( );

	glFlush ( );



}
int main (int argc, char** argv)
{
	glutInit (&argc, argv);
	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
	glutInitWindowPosition (10, 30);
	glutInitWindowSize (750, 750);
	glutCreateWindow ("CSL7450: Implementing the supersampling technique");
	init ( );
	glutDisplayFunc (TriangleRaster);
	glutMainLoop ( );
}