package com.java.movingobstacle;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Canvas;
import android.view.View;
import android.widget.Toast;

import com.java.movingobstacle.Algorithm.BaseRules;
import com.java.movingobstacle.Model.Obstacle;
import com.java.movingobstacle.Model.Point;
import com.java.movingobstacle.Model.Robot;
import com.java.movingobstacle.Model.Vector;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class MovingObstaclesView extends View {
    private Robot robot;
    private List<Obstacle> obstacleList ;
    private int canvasWidth;
    private int canvasHeight;
    private int totalFrame =0;
    private Boolean isForward = false;
    private Boolean isFinish = false;
    private Boolean islimit = false;
    private Bitmap background;
    private BaseRules baseRules ;

    public MovingObstaclesView(Context context) {
        super(context);
        Bitmap bp_robot = BitmapFactory.decodeResource(getResources(), R.drawable.robot);
        robot = new Robot("Robot", bp_robot);
        obstacleList = new ArrayList<>();
        Bitmap bp_object[] = {BitmapFactory.decodeResource(getResources(), R.drawable.object_0),
                BitmapFactory.decodeResource(getResources(), R.drawable.object_1),
                BitmapFactory.decodeResource(getResources(), R.drawable.object_2),
                BitmapFactory.decodeResource(getResources(), R.drawable.object_3),
                BitmapFactory.decodeResource(getResources(), R.drawable.object_4),
                BitmapFactory.decodeResource(getResources(), R.drawable.object_5),
                BitmapFactory.decodeResource(getResources(), R.drawable.object_6),
                BitmapFactory.decodeResource(getResources(), R.drawable.object_7)
        };
        Random generator = new Random(19900828);
        Obstacle obstacle[] = {
                new Obstacle("Obstacle 0", new Point(0,0), 1, new Vector(1,1), bp_object[0]),
                new Obstacle("Obstacle 1", new Point(0,0), 1, new Vector(3,2), bp_object[1]),
                new Obstacle("Obstacle 2", new Point(21,22), 1, new Vector(1,6), bp_object[2]),
                new Obstacle("Obstacle 3", new Point(70,10), 1, new Vector(3,1), bp_object[3]),
                new Obstacle("Obstacle 4", new Point(170,100), 1, new Vector(-1,0), bp_object[4]),
                new Obstacle("Obstacle 5", new Point(12,10), 4, new Vector(4,5), bp_object[5]),
                new Obstacle("Obstacle 6", new Point(20,0), 1, new Vector(1,2), bp_object[6]),
                new Obstacle("Obstacle 7", new Point(8,29), 1, new Vector(0,1), bp_object[7]),


                /*new Obstacle("Obstacle 0", new Point(generator.nextInt(120),generator.nextInt(120)), 1, new Vector(generator.nextInt(10) -5,generator.nextInt(8) -4), bp_object[0]),
                new Obstacle("Obstacle 1", new Point(generator.nextInt(120),generator.nextInt(120)), 1, new Vector(generator.nextInt(10) -5,generator.nextInt(8) -4), bp_object[1]),
                new Obstacle("Obstacle 2", new Point(generator.nextInt(120),generator.nextInt(120)), 1, new Vector(generator.nextInt(10) -5,generator.nextInt(8) -4), bp_object[2]),
                new Obstacle("Obstacle 3", new Point(generator.nextInt(120),generator.nextInt(120)), 1, new Vector(generator.nextInt(10) -5,generator.nextInt(8) -4), bp_object[3]),
                new Obstacle("Obstacle 4", new Point(generator.nextInt(120),generator.nextInt(120)), 1, new Vector(generator.nextInt(10) -5,generator.nextInt(8) -4), bp_object[4]),
                new Obstacle("Obstacle 5", new Point(generator.nextInt(120),generator.nextInt(120)), 4, new Vector(generator.nextInt(10) -5,generator.nextInt(8) -4), bp_object[5]),
                new Obstacle("Obstacle 6", new Point(generator.nextInt(120),generator.nextInt(120)), 1, new Vector(generator.nextInt(10) -5,generator.nextInt(8) -4), bp_object[6]),
                new Obstacle("Obstacle 7", new Point(generator.nextInt(120),generator.nextInt(120)), 1, new Vector(generator.nextInt(10) -5, generator.nextInt(8) -4), bp_object[7]),
        */
        };
        for(int i = obstacle.length -1; i >=0;  i --){
            obstacleList.add(obstacle[i]);
        }
        background = BitmapFactory.decodeResource(getResources(), R.drawable.background);
        baseRules = new BaseRules();
    }
    private int count = 0;

    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        canvasWidth = canvas.getWidth();
        canvasHeight = canvas.getHeight();
        totalFrame ++;
        canvas.drawBitmap(background, 0, 0, null);
        canvas.drawBitmap(robot.getBitmap(), robot.getCurrent().getX() / 200 * canvasWidth, robot.getCurrent().getY() / 250* canvasHeight , null);
        for (int i = 0; i < obstacleList.size(); i ++){
            Obstacle obstacle = obstacleList.get(i);
            canvas.drawBitmap(obstacle.getBitmap(), obstacle.getCurrent().getX() / 200 * canvasWidth, obstacle.getCurrent().getY() / 250* canvasHeight , null);
        }
        if(totalFrame >= 10 && !isFinish){
            robot.updatePoint(0, islimit);
            robot.updatePoint(1, islimit);
            robot.updatePoint(2, islimit);
            if(count >0) count --;
            if(count ==0)
                islimit = robot.getCurrent().getX() / 200 * canvasWidth<0 || robot.getCurrent().getX()/ 200 * canvasWidth > canvasWidth - 2 * robot.getBitmap().getWidth();
            if(Math.abs(robot.getCurrent().getY() / 250* canvasHeight - canvasHeight) < 10){
                isFinish = true;
            }
            if(robot.getVector().getY() < 0){
                robot.getVector().setY(- robot.getVector().getY());
            }

            for(int i = 0; i < obstacleList.size(); i ++){
                obstacleList.get(i).updatePoint();
                obstacleList.get(i).updatePoint();
                obstacleList.get(i).updatePoint();
            }
            canvas.drawBitmap(robot.getBitmap(), robot.getCurrent().getX() / 200 * canvasWidth, robot.getCurrent().getY() / 250* canvasHeight , null);
            for (int i = 0; i < obstacleList.size(); i ++){
                Obstacle obstacle = obstacleList.get(i);
                canvas.drawBitmap(obstacle.getBitmap(), obstacle.getCurrent().getX() / 200 * canvasWidth, obstacle.getCurrent().getY() / 250* canvasHeight , null);
            }


            for(int i = 0; i < obstacleList.size(); i ++){
                float angle = robot.angle(obstacleList.get(i).getVector());
                float distance = robot.distance(obstacleList.get(i).getCurrent());
                int rule = BaseRules.getDirection((int)distance, (int)angle);
                Vector deviation = new Vector(0,0);
                switch (rule){
                    case BaseRules.FORWARD:
                        isForward = true;
                        break;
                    case BaseRules.FORWARD_LEFT:
                        if (robot.getVector().getX() ==0 && robot.getVector().getY() >0){
                            if(!islimit){
                                deviation.setX((float) (-1/ Math.sqrt(2)));
                            } else {
                                deviation.setX((float) (1/ Math.sqrt(2)));
                            }
                            deviation.setY(0);

                        } else if (robot.getVector().getX() ==0 && robot.getVector().getY() <0){
                            if(!islimit){
                                deviation.setX((float) (1/ Math.sqrt(2)));
                            } else{
                                deviation.setX((float) (-1/ Math.sqrt(2)));
                            }
                            deviation.setY(0);

                        }else if (robot.getVector().getX() <0 && robot.getVector().getY() ==0){
                            if(!islimit){
                                deviation.setX(0);
                                deviation.setY((float) (-1/ Math.sqrt(2)));
                            } else{
                                deviation.setX(0);
                                deviation.setY((float) (1/ Math.sqrt(2)));
                            }
                        }
                        else if (robot.getVector().getX() >0 && robot.getVector().getY() ==0){
                            if(!islimit){
                                deviation.setX(0);
                                deviation.setY((float) (1/ Math.sqrt(2)));
                            } else{
                                deviation.setX(0);
                                deviation.setY((float) (-1/ Math.sqrt(2)));
                            }

                        } else if ((robot.getVector().getX() >0 && robot.getVector().getY() >0) || (robot.getVector().getX() <0 && robot.getVector().getY() >0)){
                            if(!islimit){
                                deviation.setX((float) (-1/ Math.sqrt(2)));
                                deviation.setY((float) (1/ Math.sqrt(2)) * robot.getVector().getX() / robot.getVector().getY());
                            } else{
                                deviation.setX((float) (1/ Math.sqrt(2)));
                                deviation.setY((float) (-1/ Math.sqrt(2)) * robot.getVector().getX() / robot.getVector().getY());
                            }

                        }else if ((robot.getVector().getX() >0 && robot.getVector().getY() >0) || (robot.getVector().getX() <0 && robot.getVector().getY() >0)){
                            if(!islimit){
                                deviation.setX((float) (1/ Math.sqrt(2)));
                                deviation.setY((float) (-1/ Math.sqrt(2)) * robot.getVector().getX() / robot.getVector().getY());
                            } else{
                                deviation.setX((float) (-1/ Math.sqrt(2)));
                                deviation.setY((float) (1/ Math.sqrt(2)) * robot.getVector().getX() / robot.getVector().getY());
                            }
                        }
                        islimit = false;
                        count = 2;
                        break;

                    case BaseRules.FORWARD_RIGHT:
                        if (robot.getVector().getX() ==0 && robot.getVector().getY() >0){
                            if(islimit){
                                deviation.setX((float) (-1/ Math.sqrt(2)));
                            } else {
                                deviation.setX((float) (1/ Math.sqrt(2)));
                            }
                            deviation.setY(0);

                        } else if (robot.getVector().getX() ==0 && robot.getVector().getY() <0){
                            if(islimit){
                                deviation.setX((float) (1/ Math.sqrt(2)));
                            } else{
                                deviation.setX((float) (-1/ Math.sqrt(2)));
                            }
                            deviation.setY(0);

                        }else if (robot.getVector().getX() <0 && robot.getVector().getY() ==0){
                            if(islimit){
                                deviation.setX(0);
                                deviation.setY((float) (-1/ Math.sqrt(2)));
                            } else{
                                deviation.setX(0);
                                deviation.setY((float) (1/ Math.sqrt(2)));
                            }
                        }
                        else if (robot.getVector().getX() >0 && robot.getVector().getY() ==0){
                            if(islimit){
                                deviation.setX(0);
                                deviation.setY((float) (1/ Math.sqrt(2)));
                            } else{
                                deviation.setX(0);
                                deviation.setY((float) (-1/ Math.sqrt(2)));
                            }

                        } else if ((robot.getVector().getX() >0 && robot.getVector().getY() >0) || (robot.getVector().getX() <0 && robot.getVector().getY() >0)){
                            if(islimit){
                                deviation.setX((float) (-1/ Math.sqrt(2)));
                                deviation.setY((float) (1/ Math.sqrt(2)) * robot.getVector().getX() / robot.getVector().getY());
                            } else{
                                deviation.setX((float) (1/ Math.sqrt(2)));
                                deviation.setY((float) (-1/ Math.sqrt(2)) * robot.getVector().getX() / robot.getVector().getY());
                            }

                        }else if ((robot.getVector().getX() >0 && robot.getVector().getY() >0) || (robot.getVector().getX() <0 && robot.getVector().getY() >0)){
                            if(islimit){
                                deviation.setX((float) (1/ Math.sqrt(2)));
                                deviation.setY((float) (-1/ Math.sqrt(2)) * robot.getVector().getX() / robot.getVector().getY());
                            } else{
                                deviation.setX((float) (-1/ Math.sqrt(2)));
                                deviation.setY((float) (1/ Math.sqrt(2)) * robot.getVector().getX() / robot.getVector().getY());
                            }
                        }
                        islimit = false;
                        count = 2;
                        break;
                }
                robot.getVector().setX(robot.getVector().getX() + deviation.getX());
                robot.getVector().setY(robot.getVector().getY() + deviation.getY());
            }
            totalFrame = 0;
        }

        if(isFinish == true){
            Toast.makeText(getContext(), "The robot's reached the target!", Toast.LENGTH_SHORT).show();
            isFinish = false;
        }
    }
}
