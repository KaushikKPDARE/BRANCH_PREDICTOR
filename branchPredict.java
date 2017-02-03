import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Collections;
import java.util.*;

public class Recordone {
    public static void main(String[] args) {
	 int predict=0, mispredict =0;
      Recordone one = new Recordone();
    File file = new File("address.txt");
		        ArrayList<Integer> add=new ArrayList<Integer>();
				ArrayList<Integer> def=new ArrayList<Integer>();
				int diff=0, diff1=0;
				int key;
            Scanner scanner = new Scanner(file);
            while (scanner.hasNextLine()) {
                   String line = scanner.nextLine();
				   add.add(line);
				   }
				   int len = add.size();
				   for(int i=0;i<len;i++){
				    diff = add.get(i+1)-add.get(i);
					if(diff>15 || diff<0){
					 def.add(add.get(i));
					}
				   }
				   int len1 = def.size();
				   def = one.removeDuplicate(def);
				   
				   ArrayList<Integer> dd=new ArrayList<Integer>();
				   for(int i=0; i<len;i++){
				   for(int j=0;j<def1.size();j++){
				    diff1 = add.get(i+1)-add.get(i);
					if(def1.get(j)==add.get(i)){
					 if(diff>15 || diff<0){
					 predict = predict+1;
					}
					else{
					 mispredict = mispredict+1;
					}
				   }
				   }
				   System.out.println("Predict: "+predict+" Mispredict: "+mispredict);
	}
	
	public int removeDuplicate(ArrayList<Integer> def1){
	ArrayList<Integer> sam=new ArrayList<Integer>();
	 for(int i=0;i<def1.size;i++){
	  if(!sam.contains(def1.get(i))){
	   sam.add(def1.get(i));
	  }
	}
	}