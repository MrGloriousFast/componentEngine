#version 330
out vec4 outcolor;

uniform sampler2D diffuse;

in vec2 texcord0;


void main(){
    //r,g,b,alpha
    //outColor = texture(samplerTex1, outTexCord)*color;
    //outColor = mix(texture(samplerTex1, outTexCord), texture(samplerTex2, outTexCord), 0.2);
    //outColor = color;
    outcolor = texture2D(diffuse, texcord0);
}
