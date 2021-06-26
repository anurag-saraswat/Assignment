#include <GL/glut.h> // (or others, depending on the system in use)

void init (void)
{
	glClearColor (1.0, 1.0, 1.0, 0.0); // Set display-window color to white.
	glMatrixMode (GL_PROJECTION); // Set projection parameters.
	gluOrtho2D (0.0, 500.0, 0.0, 500.0);
}

void dispPoint (void)
{
	glClear (GL_COLOR_BUFFER_BIT); // Clear display window.
	glColor3f (1.0, 0.0, 0.0); // Set point color to green.
	glPointSize(20.0f); 
	glBegin(GL_TRIANGLES);
	glVertex2i (50, 50); // Specify point location.
	glVertex2i (250, 200);
	glVertex2i (50, 100); // Specify point location.
	glEnd();
	glutSwapBuffers();
	glFlush(); 
}
int main (int argc, char** argv)
{
	glutInit (&argc, argv); // Initialize GLUT.
	glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB); // Set display mode.
	glutInitWindowPosition (20, 20); // Set top-left display-window position.
	glutInitWindowSize (500, 500); // Set display-window width and height.
	glutCreateWindow("CSL7450: Example 2"); // Create display window.
	init ( ); // Execute initialization procedure.
	glutDisplayFunc (dispPoint); // Send graphics to display window.
	glutMainLoop ( ); // Display everything and wait.
}
