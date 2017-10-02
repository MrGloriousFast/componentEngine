#version 330
in vec3 inposition; //vertex position
in vec2 intexcord;
in vec3 incord;


out vec2 texcord0;
        
void main(){
    
    //gl_Position = vec4(inposition, 1.0f);                     gl_Position = vec4(inposition.x+incord.x,inposition.y+incord.y,inposition.z+incord.z, 1.0f);
    gl_Position = vec4( inposition.x,
                        inposition.y,
                        inposition.z         , 1.0f);
    //color = vec4(0.5f,0.5f,0.5f,1.0f);
    texcord0 = intexcord;
}
