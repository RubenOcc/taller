$(document).ready(function () {
  $('#clients').DataTable({
    ajax: {
      url: '/client/list',
      type: 'GET',
      dataType: 'json',
      dataSrc: '' 
    },
    responsive: true,
    paging: true,
    searching: true,
    ordering: true,
    language: {
      url: '//cdn.datatables.net/plug-ins/2.3.0/i18n/es-ES.json'
    },
    columns: [
      { data: 'first_name', title: 'Nombres' },
      {
        data: null,
        title: 'Apellidos',
        render: function (data, type, row) {
          return `${row.last_name_father} ${row.last_name_mother}`;
        }
      },
      { data: 'address', title: 'Dirección' },
      { data: 'reference', title: 'Referencia' },
      { data: 'phone', title: 'Celular' },
      { data: 'district', title: 'Distrito' },
      {
        data: 'created_at',
        title: 'Fecha de registro',
        render: function (data) {
          return new Date(data).toLocaleDateString();
        }
      }
    ]
  });
});
