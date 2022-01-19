package demo;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class GetNumber2Test {

	@Test
	void test1() {
		// Given
		int x = 2;
		int c = 1;
		
		// When
		long expected = 2;
		long actual = Main.getNumber(x, c);
		
		// Then
		assertEquals(expected, actual);
	}
	
	@Test
	void test2() {
		// Given
		int x = 2;
		int c = 2;
		
		// When
		long expected = 20;
		long actual = Main.getNumber(x, c);
		
		// Then
		assertEquals(expected, actual);
	}
	
	@Test
	void test3() {
		// Given
		int x = 2;
		int c = 3;
		
		// When
		long expected = 200;
		long actual = Main.getNumber(x, c);
		
		// Then
		assertEquals(expected, actual);
	}
	
	@Test
	void test4() {
		// Given
		int x = 2;
		int c = 4;
		
		// When
		long expected = 2_000;
		long actual = Main.getNumber(x, c);
		
		// Then
		assertEquals(expected, actual);
	}
	
	@Test
	void test5() {
		// Given
		int x = 2;
		int c = 5;
		
		// When
		long expected = 20_000;
		long actual = Main.getNumber(x, c);
		
		// Then
		assertEquals(expected, actual);
	}
	
	@Test
	void test6() {
		// Given
		int x = 2;
		int c = 6;
		
		// When
		long expected = 200_000;
		long actual = Main.getNumber(x, c);
		
		// Then
		assertEquals(expected, actual);
	}
	
	@Test
	void test7() {
		// Given
		int x = 2;
		int c = 7;
		
		// When
		long expected = 2_000_000;
		long actual = Main.getNumber(x, c);
		
		//Then
		assertEquals(expected, actual);
	}
	
	@Test
	void test8() {
		// Given
		int x = 2;
		int c = 8;
		
		// When
		long expected = 20_000_000;
		long actual = Main.getNumber(x, c);
		
		// Then
		assertEquals(expected, actual);
	}
	
	@Test
	void test9() {
		// Given
		int x = 2;
		int c = 9;
		
		// When
		long expected = 200_000_000;
		long actual = Main.getNumber(x, c);
		
		// Then
		assertEquals(expected, actual);
	}
	
	@Test
	void test10() {
		// Given
		int x = 2;
		int c = 10;
		
		// When
		long expected = 2_000_000_000;
		long actual = Main.getNumber(x, c);
		
		// Then
		assertEquals(expected, actual);
	}

}
