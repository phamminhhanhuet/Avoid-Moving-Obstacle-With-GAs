package com.java.movingobstacle.Model;

import android.graphics.Bitmap;
import android.util.Log;
import java.lang.Math;
public class Obstacle {
    private String mName;
    private Point mStart;
    private float mVelocity;
    private Point mCurrent;
    private Point mPast;
    private Vector mVector;

    private Bitmap mBitmap;

    public Obstacle( String mName, Point mStart, float mVelocity,  Vector mVector, Bitmap mBitmap) {
        this.mVelocity = mVelocity;
        this.mStart = mStart;
        this.mCurrent = mStart;
        this.mPast = mCurrent;
        this.mVector = mVector;
        this.mName = mName;
        this.mBitmap = mBitmap;
    }

    public void setBitmap(Bitmap mBitmap){
        this.mBitmap = mBitmap;
    }
    public void setVelocity(float mVelocity) {
        this.mVelocity = mVelocity;
    }

    public void setPast(Point mPast) {
        this.mPast = mPast;
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
    public Point getPast() {
        return mPast;
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

    public void updatePoint(){
        Log.d("ValueError", "point and vector must to have same size");
        assert(mCurrent.size() == mVector.size());
        float way = mVelocity * 1 ; // 1 don vi thoi gian
        float vt_len = (float) Math.sqrt(Math.pow(mVector.getX(), 2) + Math.pow(mVector.getY(), 2));
        float deviation = way / vt_len;
        mPast = mCurrent;
        mCurrent.setX(mCurrent.getX() + mVector.getX() * deviation);
        mCurrent.setY(mCurrent.getY() + mVector.getY() * deviation);
    }
}
