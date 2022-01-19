package demo;

public class Main {

	public static void main(String[] args) {
		
		long max = 0;
		
		for (int x1 = 1; x1 < 10; x1++) {
			System.out.println("x1 = " + x1);
			for (int x2 = 0; x2 < 10; x2++) {
				if (valid(x1, x2) && notDublicate(x1, x2)) {
					for (int x3 = 0; x3 < 10; x3++) {
						if (valid(x2, x3) && notDublicate(x1, x2, x3)) {
							for (int x4 = 0; x4 < 10; x4++) {
								if (valid(x3, x4) && notDublicate(x1, x2, x3, x4)) {
									for (int x5 = 0; x5 < 10; x5++) {
										if (valid(x4, x5) && notDublicate(x1, x2, x3, x4, x5)) {
											for (int x6 = 0; x6 < 10; x6++) {
												if (valid(x5, x6) && notDublicate(x1, x2, x3, x4, x5, x6)) {
													for (int x7 = 0; x7 < 10; x7++) {
														if (valid(x6, x7) && notDublicate(x1, x2, x3, x4, x5, x6, x7)) {
															for (int x8 = 0; x8 < 10; x8++) {
																if (valid(x7, x8) && notDublicate(x1, x2, x3, x4, x5, x6, x7, x8)) {
																	for (int x9 = 0; x9 < 10; x9++) {
																		if (valid(x8, x9) && notDublicate(x1, x2, x3, x4, x5, x6, x7, x8, x9)) {
																			for (int x10 = 0; x10 < 10; x10++) {
																				if (valid(x9, x10) && notDublicate(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10)) {
																					long cur = getNumber(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10);
																					if (cur > max) {
																						max = cur;
																					}
																				}
																			}
																		}
																	}
																}
															}
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
		
		System.out.println("Ok");
		System.out.println("max = " + max);
	}
	
	public static boolean notDublicate(int ...args) {
		boolean result = true;
		for (int i = 0; i < args.length; i++) {
			for (int j = 0; j < args.length; j++) {
				if (i != j) {
					if (args[i] == args[j]) {
						result = false;
					}
				}
			}
		}
		return result;
	}
	
	public static boolean valid(int a, int b) {
		boolean result = true;
		if (a == b) {
			result = false;
		} else {
			if (a != 0 && b != 0) {
				if (! (isZ(a, b) || isZ(b, a))) {
					result = false;
				}
			} else {
				if (a != 0) {
					if (!isZ(b, a)) {
						result = false;
					}
				} else {
					if (b != 0) {
						if (!isZ(a, b)) {
							result = false;
						}
					}
				}
			}
		}
		return result;
	}
	
	
	public static boolean isZ(int a, int b) {
		boolean result = true;
		double a1 = (double) a / (double) b;
		double a2 = a / b;
		result = a1 == a2;
		return result;
	}
	
	public static long getNumber(int x1, int x2, int x3, int x4, int x5, int x6, int x7, int x8, int x9, int x10) {
		long result = 0;
		result += getNumber(x1, 10);
		result += getNumber(x2, 9);
		result += getNumber(x3, 8);
		result += getNumber(x4, 7);
		result += getNumber(x5, 6);
		result += getNumber(x6, 5);
		result += getNumber(x7, 4);
		result += getNumber(x8, 3);
		result += getNumber(x9, 2);
		result += getNumber(x10, 1);
		return result;
	}
	
	public static long getNumber(int x, int razryad) {
		long t = (long) Math.pow(10, razryad - 1);
		return x * t;
	}
}
