public class SierpinskiTree{
    
    static int base = 7;
    
    static String triangles(int n, int d, int l) {
        String result = "";
        
        for(int i =1; i<= base; i+=2) {
            for(int k = 0; k<1; k++){
                result += " ";
            }
            for(int k = 0; k<n; k++){
                for(int j = 0; j<d; j++){
                    result += " ";
                }
                for(int j = 0; j<(base - i)/2; j++){
                    result += " ";
                }
                for(int j = 0; j < (i); j++) {
                    result += "*" ;
                }
                result += " " ;
                
                for(int j = 0; j < (base - i)/2; j++) {
                    result += " " ;
                }
                for(int j = 0; j < d; j++) {
                    result += " " ;
                }
            }
            result += "\n";
            
        }
        return result ;
    }
