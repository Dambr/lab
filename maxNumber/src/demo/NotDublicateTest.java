package demo;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class NotDublicateTest {

	@Test
	void test1() {
		boolean actual = Main.notDublicate(1);
		boolean expected = true;
		assertEquals(expected, actual);
	}
	
	@Test
	void test12() {
		boolean actual = Main.notDublicate(1, 2);
		boolean expected = true;
		assertEquals(expected, actual);
	}
	
	@Test
	void test11() {
		boolean actual = Main.notDublicate(1, 1);
		boolean expected = false;
		assertEquals(expected, actual);
	}
	
	@Test
	void test121() {
		boolean actual = Main.notDublicate(1, 2, 1);
		boolean expected = false;
		assertEquals(expected, actual);
	}
	
	@Test
	void test111() {
		boolean actual = Main.notDublicate(1, 1, 1);
		boolean expected = false;
		assertEquals(expected, actual);
	}
	
	@Test
	void test1221() {
		boolean actual = Main.notDublicate(1, 2, 2, 1);
		boolean expected = false;
		assertEquals(expected, actual);
	}
	
	@Test
	void test1234567890() {
		boolean actual = Main.notDublicate(1, 2, 3, 4, 5, 6, 7, 8, 9, 0);
		boolean expected = true;
		assertEquals(expected, actual);
	}

}
