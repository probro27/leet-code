class Solution {
public:
    bool isRobotBounded(string instructions) {
        int angle = 90;
        int distanceX = 0;
        int distanceY = 0;
        for(int i = 0; i <instructions.length(); i++){
            if(instructions[i] == 'G'){
                if(angle == 90){
                    distanceY++;
                }
                else if(angle == -90){
                    distanceY--;
                }
                else if(angle == 0){
                    distanceX++;
                }
                else{
                    distanceX--;
                }
                continue;
            }
            else if(instructions[i] == 'L'){
                angle = angle + 90;
                if(angle > 180){
                    angle = 180-angle;
                }
                continue;
            }
            else{
                angle = angle-90;
                if(angle==-180){
                    angle = 180;
                }
                continue;
            }
        }
        
        if( (distanceX == 0 && distanceY == 0) || angle!=90){
            return true;
        }
        else{
            return false;
        }
    }
};