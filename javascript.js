/* Maze solution in Javascript:
   a simple program.            */

   function mark_starting_point_and_move() {
    put("token");
    while (!front_is_clear()) {
        turn_left();
    }
    move();
}

function follow_right_wall(){
    if (right_is_clear()){
        turn_right();
        move();
    } else if (front_is_clear()) {
        move();
        }
    else {
        turn_left();
    }

// Program execution below

while (!at_goal()){
    follow_right_wall();
}
