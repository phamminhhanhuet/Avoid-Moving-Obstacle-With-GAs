package com.java.movingobstacle.Algorithm;

import java.security.PublicKey;

public class BaseRules {
    private  Parameters mParameters = Parameters.getInstance();
    private static final int mRules[] = {0, 1, 1, 0, 0,
                                        0, 1, 1, 1, 1,
                                        0, 0, 1, 0, 1,
                                        1, 1, 0, 1, 1};
    public static float mDistanceThreshold = Parameters.getInstance().getDistanceThreshold();
    public static float mAngleThreshold = Parameters.getInstance().getAngleThreshold();

    public static final int FORWARD = 0;
    public static final int FORWARD_LEFT = 1;
    public static final int FORWARD_RIGHT = 2;

    private static final int VERY_NEAR = 0;
    private static final int NEAR = 1;
    private static final int FAR = 2;
    private static final int VERY_FAR = 3;

    private static final int CURRENT_LEFT = 0;
    private static final int CURRENT_FORWARD_LEFT = 1;
    private static final int CURRENT_FORWARD = 2;
    private static final int CURRENT_FORWARD_RIGHT = 3;
    private static final int CURRENT_RIGHT = 4;

    public int[] getRules() {
        return mRules;
    }

    public float getDistanceThreshold(){
        return mParameters.getDistanceThreshold();
    }

    public float getAngleThreshold(){
        return mParameters.getAngleThreshold();
    }

    public static int getDirection(int distance, int angle){
        int status_dis = -1;
        int status_agl = -1;
        double choice = Math.random();
        if (distance <= (mDistanceThreshold -2)/ 3){
            status_dis = choice > 0.5? VERY_NEAR : NEAR;
        } else if (distance<= 2 + mDistanceThreshold /3 * 2){
            status_dis = choice > 0.5? NEAR: FAR;
        } else if (distance<= 2 + mDistanceThreshold){
            status_dis = choice> 0.5?FAR: VERY_FAR;
        } else if (distance > 2+ mDistanceThreshold){
            status_dis = VERY_FAR;
        }
        choice = Math.random();
        if(angle < - mAngleThreshold){
            status_agl = CURRENT_LEFT;
        } else if (angle <= -mAngleThreshold / 2){
            status_agl = choice > 0.5? CURRENT_LEFT:CURRENT_FORWARD_LEFT;
        }else if(angle <= 0.0){
            status_agl = choice>0.5? CURRENT_FORWARD_LEFT: CURRENT_FORWARD;
        } else if (angle <= mAngleThreshold /2){
            status_agl = choice>0.5? CURRENT_FORWARD: CURRENT_FORWARD_RIGHT;
        } else if (angle <= mAngleThreshold){
            status_agl = choice>0.5? CURRENT_FORWARD_RIGHT: CURRENT_RIGHT;
        } else if(angle > mAngleThreshold){
            status_agl = CURRENT_RIGHT;
        }

        if (status_agl != -1 && status_dis != -1){
            int available = mRules[status_agl * 5 + status_dis];
            if(available ==1){
                int direction = status_agl * 5 + status_dis;
                if (direction ==1 || direction == 12) return FORWARD_RIGHT;
                else if(direction ==2|| direction == 3|| direction == 7) return FORWARD_LEFT;
                else return FORWARD;
            }
        }
        return  -1;
    }
}
