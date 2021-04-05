package com.java.movingobstacle.Model;

import android.graphics.Bitmap;
import android.util.Log;

import com.java.movingobstacle.Utils.Analyze;

public class Robot {
    private String mName = "";
    private Point mStart ;
    private float mVelocity;
    private float mAccel;
    private Point mCurrent;
    private Point mEnd;
    private Vector mVector;
    private float mDeltaT;
    private Bitmap mBitmap;

    public Robot(String mName, Point mStart, Point mEnd, float mVelocity, float mAccel, Vector mVector, Bitmap mBitmap) {
        this.mVelocity = mVelocity;
        this.mStart = mStart;
        this.mCurrent = mStart;
        this.mEnd = mEnd;
        this.mAccel = mAccel;
        this.mVector = mVector;
        this.mName = mName;
        this.mBitmap = mBitmap;
    }

    public Robot(String mName, Bitmap mBitmap){
        this.mName = mName;
        this.mStart = new Point(100, 0);
        this.mCurrent = new Point(100, 0);
        this.mEnd  = new Point(100, 250);
        this.mVelocity = 0;
        this.mAccel = 1;
        this.mDeltaT = 4;
        this.mVector = new Vector(0,1);
        this.mBitmap = mBitmap;
    }

    public void setBitmap(Bitmap mBitmap){
        this.mBitmap = mBitmap;
    }

    public void setVelocity(float mVelocity) {
        this.mVelocity = mVelocity;
    }

    public void setEnd(Point mEnd) {
        this.mEnd = mEnd;
    }

    public void setCurrent(Point mCurrent) {
        this.mCurrent = mCurrent;
    }

    public void setVector(Vector mVector) {
        this.mVector = mVector;
    }

    public Bitmap getBitmap(){
        return this.mBitmap;
    }

    public Point getEnd() {
        return mEnd;
    }

    public String getName() {
        return mName;
    }

    public float getVelocity() {
        return mVelocity;
    }

    public Point getCurrent() {
        return mCurrent;
    }

    public Vector getVector() {
        return mVector;
    }

    @Override
    public String toString() {
        return "Obstacle{" +
                "mName='" + mName + '\'' +
                ", mVelocity=" + mVelocity +
                ", mCurrent=" + mCurrent +
                ", mVector=" + mVector +
                '}';
    }

    public void updatePoint(int status, boolean islimit){
        Log.d("ValueError", "point and vector must to have same size");
        assert(mCurrent.size() == mVector.size());
        mVelocity = 0;
        float vt_len = (float) Math.sqrt(Math.pow(mVector.getX(), 2) + Math.pow(mVector.getY(), 2));
        float deviation ;
        float way = mVelocity * 1 ;
        switch (status){
            case 0:
                way = (mDeltaT / 4 * mDeltaT / 4 * mAccel) * 1/2 + mDeltaT/4 * mVelocity;
                break;
            case 1:
                mVelocity = mDeltaT / 4 * mAccel + mVelocity;
                way = mVelocity * mDeltaT / 2;
                break;
            case 2:
                mVelocity = mDeltaT / 4 * mAccel + mVelocity;
                way = ((-mDeltaT /4 * mDeltaT / 4 * mAccel) * 1/2 + mDeltaT /4* mVelocity);
                break;
        }
        deviation = way / vt_len;
        if(!islimit)  mCurrent.setX(mCurrent.getX() + mVector.getX() * deviation);
        mCurrent.setY(mCurrent.getY() + mVector.getY() * deviation);
    }

    public float angle(Vector obs_vector){
        return Analyze.angle(mVector, obs_vector);
    }
    public float distance(Point obs_point){
        return (float) Math.sqrt(Math.pow(mCurrent.getX() - obs_point.getX(),2) + Math.pow(mCurrent.getY() - obs_point.getY(), 2));
    }

    public float distanceToTarget(){
        return (float) Math.sqrt(Math.pow(mCurrent.getX() - mEnd.getX(),2) + Math.pow(mCurrent.getY() - mEnd.getY(), 2));
    }
}
