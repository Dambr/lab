package demo;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class ValidTest {

	Main main;
	
	@BeforeEach
	void prepair() {
		// Given
		main = new Main();
	}
	
	@Test
	void test4_2() {
		// When
		int a = 4;
		int b = 2;
		
		// Then
		boolean expected = true;
		boolean actual = main.valid(a, b);
		assertEquals(expected, actual);
	}
	
	@Test
	void test0_2() {
		// When
		int a = 0;
		int b = 2;
		
		// Then
		boolean expected = true;
		boolean actual = main.valid(a, b);
		assertEquals(expected, actual);
	}
	
	@Test
	void test2_0() {
		// When
		int a = 2;
		int b = 0;
		
		// Then
		boolean expected = true;
		boolean actual = main.valid(a, b);
		assertEquals(expected, actual);
	}
	
	@Test
	void test3_2() {
		// When
		int a = 3;
		int b = 2;
		
		// Then
		boolean expected = false;
		boolean actual = main.valid(a, b);
		assertEquals(expected, actual);
	}
	
	@Test
	void test2_3() {
		// When
		int a = 2;
		int b = 3;
		
		// Then
		boolean expected = false;
		boolean actual = main.valid(a, b);
		assertEquals(expected, actual);
	}
	
	@Test
	void test3_3() {
		// When
		int a = 3;
		int b = 3;
		
		// Then
		boolean expected = false;
		boolean actual = main.valid(a, b);
		assertEquals(expected, actual);
	}
	
	@Test
	void test0_0() {
		// When
		int a = 0;
		int b = 0;
		
		// Then
		boolean expected = false;
		boolean actual = main.valid(a, b);
		assertEquals(expected, actual);
	}

}
