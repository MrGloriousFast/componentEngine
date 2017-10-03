#version 330
in vec3 inposition; //vertex position
in vec2 intexcord;
in vec3 incord;
in float scale;

out vec2 texcord0;
        
void main(){
    

//    gl_Position = vec4( inposition.x+incord.x,
//                        inposition.y+incord.y,
//                        inposition.z+incord.z, 1.0f);
//
//    gl_Position = vec4( scale*inposition.x+incord.x,
//                        scale*inposition.y+incord.y,
//                        inposition.z+incord.z, 1.0f);


    gl_Position = vec4( scale*inposition+incord, 1.0f);


    texcord0 = intexcord;
}
