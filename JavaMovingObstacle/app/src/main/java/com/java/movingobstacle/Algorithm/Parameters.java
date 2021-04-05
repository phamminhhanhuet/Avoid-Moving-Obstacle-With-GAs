package com.java.movingobstacle.Algorithm;

public class Parameters {
    private float mDistanceThreshold = (float) 14.56;
    private float mAngleThreshold = (float) 55.54 * 2;

    public float getDistanceThreshold() {
        return mDistanceThreshold;
    }

    public float getAngleThreshold() {
        return mAngleThreshold;
    }

    private static Parameters INSTANCE = new Parameters();
    public static Parameters  getInstance(){
        if (INSTANCE == null) {
            // Do the task too long before create instance ...
            // Block so other threads cannot come into while initialize
            synchronized (Parameters.class) {
                // Re-check again. Maybe another thread has initialized before
                if (INSTANCE == null) {
                    INSTANCE = new Parameters();
                }
            }
        }
        // Do something after get instance ...
        return INSTANCE;
    }

}
