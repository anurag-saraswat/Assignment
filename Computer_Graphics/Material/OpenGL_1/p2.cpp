#include <GL/glut.h> // (or others, depending on the system in use)

void init (void)
{
	glClearColor (0.0, 0.0, 0.0, 0.0); // Set display-window color to white.
	glMatrixMode (GL_PROJECTION); // Set projection parameters.
	gluOrtho2D (0.0, 500.0, 0.0, 500.0);
}

void dispPoint (void)
{
	glClear (GL_COLOR_BUFFER_BIT); // Clear display window.
	glColor3f (0.0, 1.0, 0.0); // Set point color to green.
	//glPointSize(1.0f); 
	glBegin(GL_LINES);
	glVertex2i (100, 100); // Specify point location.
	glVertex2i (500, 400);
	glVertex2i (100, 200); // Specify point location.
	glVertex2i (500, 400);
	glVertex2i (100, 300); // Specify point location.
	glVertex2i (500, 400);
	glEnd();
	glFlush(); 
}
int main (int argc, char** argv)
{
	glutInit (&argc, argv); // Initialize GLUT.
	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB); // Set display mode.
	glutInitWindowPosition (20, 20); // Set top-left display-window position.
	glutInitWindowSize (500, 500); // Set display-window width and height.
	glutCreateWindow("CSL7450: Example 2"); // Create display window.
	init ( ); // Execute initialization procedure.
	glutDisplayFunc (dispPoint); // Send graphics to display window.
	glutMainLoop ( ); // Display everything and wait.
}
