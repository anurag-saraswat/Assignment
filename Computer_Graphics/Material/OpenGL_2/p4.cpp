#include <GL/glut.h> // 
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

void init (void)
{
glClearColor (1.0, 1.0, 1.0, 0.0); // display window color .
glMatrixMode (GL_PROJECTION); // projection parameters.
glLoadIdentity();
gluOrtho2D (0.0,500.0,0.0,500.0);
}
void circileIUA(void)
{   
    glClear (GL_COLOR_BUFFER_BIT); // Clear display window.
    glColor3f (0.0, 0.0, 0.0);
    GLint x, y;    
    
    glBegin (GL_POINTS);
	    for (x = 0; x <=400; x++) {
	    	y= sqrt(160000-x*x);
	        y= int(y+0.5);
	        glVertex2i (x, y);
	    }
    glEnd ( );

    glFlush ( ); 
}
int main (int argc, char** argv)
{
    glutInit (&argc, argv); // Initialize GLUT.
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB); // Set display mode.
    glutInitWindowPosition (20, 20); // Set top-left display-window position.
    glutInitWindowSize (500, 500); // Set display-window width and height.
    glutCreateWindow ("CSL7450: Incremental Circle Drawing"); // Create display window.
    init ( ); // Execute initialization procedure.
    glutDisplayFunc (circileIUA); // Send graphics to display window.
    glutMainLoop ( ); // Display everything and wait.
}