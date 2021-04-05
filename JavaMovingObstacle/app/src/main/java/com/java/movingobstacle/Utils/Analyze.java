package com.java.movingobstacle.Utils;
import com.java.movingobstacle.Model.Point;
import com.java.movingobstacle.Model.Vector;

import java.lang.Math;

import static java.lang.Math.atan2;

public class Analyze {
    public static float angle(Vector a, Vector b){
        float angle = (float) atan2( a.getX()*b.getY() - a.getY()*b.getX(), a.getX()*b.getX() + a.getX()*b.getX() );
        if(a.getX()*b.getY() - a.getY()*b.getX() < 0)
            angle = -angle;
        return  angle;
    }

    public static float distance(Point a, Point b){
        return (float) Math.sqrt(Math.pow(a.getX() - b.getX(),2) + Math.pow(a.getY() - b.getY(), 2));
    }


}
