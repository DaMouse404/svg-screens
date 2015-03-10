#include <stdio.h>
#include <stdint.h>

#define SCREEN_SHAPE_TYPE_RECT 1
#define SCREEN_SHAPE_TYPE_CIRCLE 2

typedef struct screen_colour {
	uint8_t background_r;
	uint8_t background_g;
	uint8_t background_b;
} screen_colour;

struct screen_shape {
	unsigned id : 4;
	unsigned type : 4;
	screen_colour colour;
	struct screen_shape *next;
};
typedef struct screen_shape screen_shape;

typedef struct screen_shape_rect {
	screen_shape super;
	uint16_t startx;
	uint16_t starty;
	uint16_t endx;
	uint16_t endy;
} screen_shape_rect;

typedef struct screen {
	screen_shape *shape;
	screen_colour background;
} screen;

#include "test.h"

int main() {
	screen_shape *shape = (screen_shape *) &screen_menu_shape_4;
	screen_shape_rect *shape_rect = (screen_shape_rect *) &screen_menu_shape_4;

	while (shape != NULL) {
		printf("x: %d, y: %d\n", shape_rect->endx, shape_rect->endy);

		shape = (screen_shape *) shape->next;
		shape_rect = (screen_shape_rect *) shape;
	};

	return 0;
}
