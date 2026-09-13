Markdown# 📊 PORTAFOLIO DE CIENCIA DE DATOS: HR Analytics & Performance Power BI Model

Repositorio dedicado al análisis avanzado de Recursos Humanos, gestión del desempeño y retención de talento (*Attrition Analytics*), estructurado como un modelo de Business Intelligence profesional en Power BI complementado con análisis de datos en Python y modelado relacional en estrella (*Star Schema*).

---

## 🛠️ Estructura del Repositorio y Archivos del Proyecto

```text
├── HR Analytics.pbix                 # Modelo principal de Power BI (.pbix)
├── Employee.csv                      # Dimensión de empleados (1,470 registros)
├── PerformanceRating.csv             # Tabla de hechos de evaluaciones y satisfacción (6,709 registros)
├── DimDate.txt                       # Script DAX para la generación de la dimensión temporal
├── EducationLevel.csv                # Catálogo normalizado de niveles educativos
├── RatingLevel.csv                   # Catálogo normalizado de niveles de calificación
├── SatisfiedLevel.csv                # Catálogo normalizado de niveles de satisfacción
└── Informe_Detallado_PowerBI_HR.pdf  # Documentación técnica y funcional completa del reporte
🧠 Arquitectura del Modelo de Datos (Star Schema)El proyecto implementa un modelo dimensional relacional optimizado para consultas analíticas de alto rendimiento en Power BI:DimEmployee (Tabla de Dimensión Principal): Contiene 1,470 registros con información demográfica, rol laboral, departamento, salario, antigüedad y estado de rotación (Attrition).PerformanceRating (Tabla de Hechos): Contiene 6,709 registros históricos de evaluaciones de desempeño, autoevaluaciones, métricas de clima laboral, conciliación (Work-Life Balance) y oportunidades de capacitación.DimDate (Dimensión Temporal): Tabla de fechas generada mediante código DAX dinámico (CALENDAR) enlazada a las fechas de contratación y revisión.Tablas de Catálogo Normalizadas (EducationLevel, RatingLevel, SatisfiedLevel): Permiten la traducción limpia de códigos numéricos a etiquetas cualitativas estándar.📑 Resumen de Páginas del Cuadro de Mando (Report View)Página del ReporteMétrica / Cálculo PrincipalObjetivo de Negocio y Análisis1. Executive Workforce OverviewTotal Employees, Active Employees, Attrition Rate, Avg SalaryPanel general de control de alto nivel para supervisar la demografía de la plantilla y la distribución de la masa salarial por departamento y rol.2. Attrition & Retention AnalyticsAttrition Count, OverTime Attrition %, análisis de distancia al hogar y estancamiento promocional.Identificación predictiva de factores de riesgo de abandono y retención preventiva de talento clave.3. Performance & Management RatingsAvg Manager Rating, Avg Self Rating, Rating DiscrepancyCalibración de revisiones de desempeño anuales, detección de sesgos en supervisiones y identificación de empleados de alto rendimiento.4. Work-Life Balance & SatisfactionAvg Job Satisfaction, Training Take-up Rate, índices de clima laboral.Evaluación del bienestar organizacional, ambiente de trabajo y el retorno de inversión en programas de formación.5. Compensation & Equity DashboardSalary Percentile 90, Total Compensation & Benefits (incluyendo StockOptionLevel).Auditoría interna de equidad retributiva y estructuración objetiva de bandas salariales y retención basada en incentivos bursátiles.⚙️ Fórmulas DAX Clave ImplementadasTasa de Rotación de Personal (Attrition Rate)Fragmento de códigoAttrition Rate = 
DIVIDE(
    CALCULATE([Total Employees], DimEmployee[Attrition] = "Yes"),
    [Total Employees]
)
Discrepancia en la Evaluación de DesempeñoFragmento de códigoRating Discrepancy = 
AVERAGE(PerformanceRating[ManagerRating]) - AVERAGE(PerformanceRating[SelfRating])
Compensación Total y BeneficiosFragmento de códigoTotal Compensation & Benefits = 
SUM(DimEmployee[Salary]) + SUMX(DimEmployee, DimEmployee[StockOptionLevel] * 1000)
🚀 Cómo Utilizar Este ProyectoClonar el repositorio:Bashgit clone [https://github.com/tu-usuario/PORTAFOLIO-DE-CIENCIA-DE-DATOS.git](https://github.com/tu-usuario/PORTAFOLIO-DE-CIENCIA-DE-DATOS.git)
Abrir el modelo:Inicia Power BI Desktop.Abre el archivo HR Analytics.pbix para interactuar con las visualizaciones y el modelo relacional.Consultar la documentación detallada:Revisa el archivo Informe_Detallado_PowerBI_HR.pdf incluido en el repositorio para ver el desglose técnico completo, especificaciones de medidas DAX y análisis de negocio por cada hoja.👩‍💻 AutorDesarrollado como parte del Portafolio de Ciencia de Datos y Business Intelligence.
