package demo;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class GetNumber10Test {

	@Test
	void test() {
		// Given
		int x1 = 1;
		int x2 = 2;
		int x3 = 3;
		int x4 = 4;
		int x5 = 5;
		int x6 = 6;
		int x7 = 7;
		int x8 = 8;
		int x9 = 9;
		int x10 = 0;
		
		// When
		long expected = 1234567890;
		long actual = Main.getNumber(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10);
		
		// Then
		assertEquals(expected, actual);
	}

}
