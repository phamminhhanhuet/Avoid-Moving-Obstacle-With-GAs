package com.java.movingobstacle;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

import java.util.Timer;
import java.util.TimerTask;

public class MainActivity extends AppCompatActivity {
    private MovingObstaclesView movingObstaclesView;
    private static final int Interval = 30;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        movingObstaclesView = new MovingObstaclesView(this);
        setContentView(movingObstaclesView);
        Timer timer = new Timer();
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                movingObstaclesView.invalidate();
            }
        }, 0, Interval);
    }
}