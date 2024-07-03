from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas as pd

# Función para cargar el contenido del archivo
template_dir = r'C:\\Users\\winde\\Documents\\python\\docs'  # Cambiar a la ruta real de tu archivo


# Crea un entorno de Jinja2 con FileSystemLoader
env = Environment(
    loader=FileSystemLoader(template_dir),
    autoescape=select_autoescape(['j2'])
)

# Nombre del archivo de template (en este caso, 'plantilla_clientes.j2')
template_file1 = 'plantilla_clientes_PPPoE.j2'
template_file2 = 'plantilla_clientes_transport.j2'

# Cargar el template desde el archivo
template1 = env.get_template(template_file1)
template2 = env.get_template(template_file2)


# Ruta al archivo Excel
excel_file = r'C:\Users\winde\Documents\python\docs\clientes.xlsx'  # Reemplaza con la ruta real de tu archivo

# Cargar datos desde Excel usando pandas
df = pd.read_excel(excel_file, sheet_name='Hoja1')

# Conjunto para mantener un registro de las configuraciones ya generadas
configuraciones_generadas = set()

# Mostrar el contenido del DataFrame para verificar
print(df.head())  # Mostrar las primeras filas para verificar que se cargaron correctamente

for index, row in df.iterrows():
    vlan_id = str(row['vlan_id'])  # Asegúrate de ajustar el nombre de la columna según tu archivo Excel
    type_service = str(row['type_service'])  # Ajustar según el nombre real de la columna en tu archivo Excel

    # Crear una clave única para esta configuración
    configuracion_actual = (vlan_id, type_service)

    # Verificar si esta configuración ya ha sido generada e impresa
    if configuracion_actual in configuraciones_generadas:
        continue  # Saltar esta configuración si ya ha sido generada


    # Determinar qué template utilizar en base a type_service
    if type_service == 'PPPoE':
        rendered_template = template1.render(vlan_id=vlan_id, type_service=type_service)
    elif type_service == 'Transporte':
        rendered_template = template2.render(vlan_id=vlan_id, type_service=type_service)
    else:
        # Manejar cualquier otro tipo de servicio aquí (si es necesario)
        continue
    # Imprimir la configuración generada
    print(rendered_template)

    # Agregar esta configuración al conjunto de configuraciones generadas
    configuraciones_generadas.add(configuracion_actual)

    #rendered_template = template.render(vlan_id=vlan_id)
    # Puedes imprimir o hacer cualquier otra operación con rendered_template aquí
    #print(rendered_template)

# Si prefieres guardar las configuraciones en archivos, puedes hacerlo así
#with open(f'config_{vlan_id}.txt', 'w') as f:
    #f.write(rendered_template)

# Definir el valor de vlan_id que deseas utilizar
#vlan_id = "123"

# Renderizar el template con el valor de vlan_id
#rendered_template = template.render(vlan_id=vlan_id)

# Imprimir la configuración generada
#print(rendered_template)