package com.design_pattern.template.game;

public class GameTest {
    public static void main(String[] args) {
        Player player = new Player(); // 처음 생성하면 Beginner Lv
        player.play(1);

        Advanced aLevel = new Advanced();
        player.upgradeLevel(aLevel);
        player.play(2);

        Super sLevel = new Super();
        player.upgradeLevel(sLevel);
        player.play(3);
    }
}
