package demo;

import java.util.Objects;
import java.util.Set;

public class Data {

	private int number;
	private Set<Set<Integer>> presents;
	
	public Data(int number, Set<Set<Integer>> presents) {
		super();
		this.number = number;
		this.presents = presents;
	}

	public Set<Set<Integer>> getPresents() {
		return presents;
	}
	
	@Override
	public int hashCode() {
		return Objects.hash(number);
	}
	
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Data other = (Data) obj;
		return number == other.number;
	}
	
}
