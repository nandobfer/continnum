<html>
  <head>
    <title>PHP Test</title>
  </head>
  <body>
<?php echo '<p>CALCULUS WITH LINGUISTIC TERMS</p>';

echo '<p>Criterion weight:</p>';

$DM_1_weight = 0.4;
$DM_2_weight = 0.3;
$DM_3_weight = 0.3;
//( )
$DM1_positive_dist_custo = $DM_1_weight * sqrt((5 - 4) + (5 - 5));
$DM2_positive_dist_custo = $DM_2_weight * sqrt((5 - 5) + (5 - 5));
$DM3_positive_dist_custo = $DM_3_weight * sqrt((3 - 3) + (4 - 4));
$sum_positive_dist_custo = $DM1_positive_dist_custo + $DM2_positive_dist_custo + $DM3_positive_dist_custo; 

$DM1_positive_dist_severidade = $DM_1_weight * sqrt((5 - 5) + (5 - 5));
$DM2_positive_dist_severidade = $DM_2_weight * sqrt((5 - 3) + (5 - 3));
$DM3_positive_dist_severidade = $DM_3_weight * sqrt((3 - 3) + (4 - 4));
$sum_positive_dist_severidade = $DM1_positive_dist_severidade + $DM2_positive_dist_severidade + $DM3_positive_dist_severidade;

$DM1_positive_dist_ocorrencia = $DM_1_weight * sqrt((5 - 3) + (5 - 3));
$DM2_positive_dist_ocorrencia = $DM_2_weight * sqrt((5 - 4) + (5 - 4));
$DM3_positive_dist_ocorrencia = $DM_3_weight * sqrt((3 - 2) + (4 - 4));
$sum_positive_dist_ocorrencia = $DM1_positive_dist_ocorrencia + $DM2_positive_dist_ocorrencia + $DM3_positive_dist_ocorrencia;
?>
      
<table border="1px" cellpadding="4" cellspacing="4">
<tr>
<td>CRITERION</td>
<td>DM1</td>
<td>DM2</td>
<td>DM3</td>
<td>SOMA (D+)</td>    
</tr>

<?php
echo "<tr>";
echo "<td>Custo</td>";
echo "<td>$DM1_positive_dist_custo</td>";
echo "<td>$DM2_positive_dist_custo</td>";
echo "<td>$DM3_positive_dist_custo</td>";
echo "<td>$sum_positive_dist_custo</td>";
echo "</tr>";

echo "<tr>";
echo "<td>Severidade</td>";
echo "<td>$DM1_positive_dist_severidade</td>";
echo "<td>$DM2_positive_dist_severidade</td>";
echo "<td>$DM3_positive_dist_severidade</td>";
echo "<td>$sum_positive_dist_severidade</td>";
echo "</tr>";

echo "<tr>";
echo "<td>Ocorrencia</td>";
echo "<td>$DM1_positive_dist_ocorrencia</td>";
echo "<td>$DM2_positive_dist_ocorrencia</td>";
echo "<td>$DM3_positive_dist_ocorrencia</td>";
echo "<td>$sum_positive_dist_ocorrencia</td>";
echo "</tr>";
?>
</table>
  
</br>

<?php

$DM1_negative_dist_custo = $DM_1_weight * sqrt((4 - 3) + (5 - 3));
$DM2_negative_dist_custo = $DM_2_weight * sqrt((5 - 3) + (5 - 3));
$DM3_negative_dist_custo = $DM_3_weight * sqrt((3 - 2) + (4 - 4));
$sum_negative_dist_custo = $DM1_negative_dist_custo + $DM2_negative_dist_custo + $DM3_negative_dist_custo; 

$DM1_negative_dist_severidade = $DM_1_weight * sqrt((5 - 3) + (5 - 3));
$DM2_negative_dist_severidade = $DM_2_weight * sqrt((3 - 3) + (3 - 3));
$DM3_negative_dist_severidade = $DM_3_weight * sqrt((3 - 2) + (4 - 4));
$sum_negative_dist_severidade = $DM1_negative_dist_severidade + $DM2_negative_dist_severidade + $DM3_negative_dist_severidade;

$DM1_negative_dist_ocorrencia = $DM_1_weight * sqrt((3 - 3) + (3 - 3));
$DM2_negative_dist_ocorrencia = $DM_2_weight * sqrt((4 - 3) + (4 - 3));
$DM3_negative_dist_ocorrencia = $DM_3_weight * sqrt((2 - 2) + (4 - 4));
$sum_negative_dist_ocorrencia = $DM1_negative_dist_ocorrencia + $DM2_negative_dist_ocorrencia + $DM3_negative_dist_ocorrencia;
?>
      
<table border="1px" cellpadding="4" cellspacing="4">
<tr>
<td>CRITERION</td>
<td>DM1</td>
<td>DM2</td>
<td>DM3</td>
<td>SOMA (D-)</td>    
</tr>

<?php

echo "<tr>";
echo "<td>Custo</td>";
echo "<td>$DM1_negative_dist_custo</td>";
echo "<td>$DM2_negative_dist_custo</td>";
echo "<td>$DM3_negative_dist_custo</td>";
echo "<td>$sum_negative_dist_custo</td>";
echo "</tr>";

echo "<tr>";
echo "<td>Severidade</td>";
echo "<td>$DM1_negative_dist_severidade</td>";
echo "<td>$DM2_negative_dist_severidade</td>";
echo "<td>$DM3_negative_dist_severidade</td>";
echo "<td>$sum_negative_dist_severidade</td>";
echo "</tr>";

echo "<tr>";
echo "<td>Ocorrencia</td>";
echo "<td>$DM1_negative_dist_ocorrencia</td>";
echo "<td>$DM2_negative_dist_ocorrencia</td>";
echo "<td>$DM3_negative_dist_ocorrencia</td>";
echo "<td>$sum_negative_dist_ocorrencia</td>";
echo "</tr>";
?>
</table>
</br>

<table border="1px" cellpadding="4" cellspacing="4">
<tr>
<td>CRITERION</td>    
<td>UNNORMALIZED</td>    
</tr>

<?php

$unnormalized_weight_custo = $sum_negative_dist_custo / ($sum_negative_dist_custo + $sum_positive_dist_custo); 
$unnormalized_weight_severidade = $sum_negative_dist_severidade / ($sum_negative_dist_severidade + $sum_positive_dist_severidade); 
$unnormalized_weight_ocorrencia = $sum_negative_dist_ocorrencia / ($sum_negative_dist_ocorrencia + $sum_positive_dist_ocorrencia);  
echo "<tr>";
echo "<td>Custo</td>";
echo "<td>$unnormalized_weight_custo</td>";
echo "</tr>";

echo "<tr>";
echo "<td>Severidade</td>";
echo "<td>$unnormalized_weight_severidade</td>";
echo "</tr>";

echo "<tr>";
echo "<td>Ocorrencia</td>";
echo "<td>$unnormalized_weight_ocorrencia</td>";
echo "</tr>";
?>
</table>

</br>

<table border="1px" cellpadding="4" cellspacing="4">
<tr>
<td>CRITERION</td>    
<td>NORMALIZED</td>    
</tr>

<?php

$sum_unnormalized_weight = $unnormalized_weight_custo + $unnormalized_weight_severidade + $unnormalized_weight_ocorrencia;

$normalized_weight_custo = $unnormalized_weight_custo / $sum_unnormalized_weight;

$normalized_weight_severidade = $unnormalized_weight_severidade / $sum_unnormalized_weight;

$normalized_weight_ocorrencia = $unnormalized_weight_ocorrencia / $sum_unnormalized_weight;
echo "<tr>";
echo "<td>Custo</td>";
echo "<td>$normalized_weight_custo</td>";
echo "</tr>";

echo "<tr>";
echo "<td>Severidade</td>";
echo "<td>$normalized_weight_severidade</td>";
echo "</tr>";

echo "<tr>";
echo "<td>Ocorrencia</td>";
echo "<td>$normalized_weight_ocorrencia</td>";
echo "</tr>";
?>
</table>      
      
<?php


?>


    <!--
    This script places a badge on your repl's full-browser view back to your repl's cover
    page. Try various colors for the theme: dark, light, red, orange, yellow, lime, green,
    teal, blue, blurple, magenta, pink!
    -->
    <script src="https://replit.com/public/js/replit-badge.js" theme="blue" defer></script> 
  </body>
</html>