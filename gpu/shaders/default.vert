#version 330
in vec3 inposition; //vertex position
in vec2 intexcord;
in vec3 incord;
in float scale;

out vec2 texcord0;

uniform vec4 camera;
        
void main(){
    
    //vec3 cam = vec3(-0.5f, -0.5f, 0.0f);

    float x = scale*inposition.x + incord.x - camera.x;
    float y = scale*inposition.y + incord.y - camera.y;
    float z = 0.0f; //scale*inposition.z + incord.z;


    gl_Position = vec4( x,y,z, 1.0f);


    texcord0 = intexcord;
}
