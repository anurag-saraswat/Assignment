
/*
 In this question we implement the midpoint circle algorithm
 Firstly, we draw the part of the circle from angle 135 degrees to 180 degrees
 Secondly, we draw the part of the circle from angle 180 degrees to 225 degrees

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
	gluOrtho2D (-250.0, 250.0, -250.0, 250.0);
}

void MidPointCircle (void)
{
	glClear (GL_COLOR_BUFFER_BIT);
	glColor3f (0.0, 0.4, 0.2);

	float r = 100;
	float x = -100 / sqrt(2);
	float y = 100 / sqrt(2);
	float d = 0;

	GLfloat a = x, b = y;

	/* To draw the centre of the circle*/
	glBegin (GL_POINTS);
	glVertex2i(a, b);
	glEnd();


	glBegin (GL_POINTS);

	/* To draw the first part of the circle
		angle from 135 degrees to 180 degrees */
	while (b > 0) {
		if (d > 0) {
			d = d - 2 * b + 3;
			b = b - 1;
		}
		else {
			d = d - 2 * a - 2 * b + 5;
			a = a - 1;
			b = b - 1;
		}
		glVertex2i(a, b);
	}

	/* To draw the first part of the circle
		angle from 180 degrees to 225 degrees */
	while (b > -(100 / sqrt(2))) {
		if (d < 0) {
			d = d - 2 * b + 3;
			b = b - 1;

		}
		else {
			d = d + 2 * a - 2 * b + 5;
			b = b - 1;
			a = a + 1;
		}
		glVertex2i(a, b);
	}
	glEnd ( );
	glFlush ( );
}
int main (int argc, char** argv)
{
	glutInit (&argc, argv);
	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
	glutInitWindowPosition (10, 30);
	glutInitWindowSize (500, 500);
	glutCreateWindow ("CSL7450: Mid Point Circle Drawing Algorithm");
	init ( );
	glutDisplayFunc (MidPointCircle);
	glutMainLoop ( );
}