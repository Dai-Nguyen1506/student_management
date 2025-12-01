// Khởi tạo modal
const modalMoreEl = document.getElementById('modalMore');
const modalMore = new bootstrap.Modal(modalMoreEl);

const modalUpdateEl = document.getElementById('modalUpdate');
const modalUpdate = new bootstrap.Modal(modalUpdateEl, {backdrop: 'static', keyboard: false});

// Lấy footer modal1 để thêm nút Save
const modalMoreFooter = modalMoreEl.querySelector('.modal-footer');

// Bấm More trong table
document.querySelectorAll('.btn-more').forEach(button => {
  button.addEventListener('click', function() {
    const id = this.getAttribute('data-id');
    const name = this.getAttribute('data-name');
    const email = this.getAttribute('data-email');
    const birth = this.getAttribute('data-birth');
    const phone = this.getAttribute('data-phone');
    const address = this.getAttribute('data-address');

    document.getElementById('modal-id').textContent = id;
    document.getElementById('modal-name').textContent = name;
    document.getElementById('modal-email').textContent = email;
    document.getElementById('modal-birth').textContent = birth;
    document.getElementById('modal-phone').textContent = phone;
    document.getElementById('modal-address').textContent = address;

    modalMore.show();
  });
});

// Bấm Update → modal2
document.getElementById('btnUpdate').addEventListener('click', function() {
  document.getElementById('update-id').value = document.getElementById('modal-id').textContent;
  document.getElementById('update-name').value = document.getElementById('modal-name').textContent;
  document.getElementById('update-email').value = document.getElementById('modal-email').textContent;
  document.getElementById('update-birth').value = document.getElementById('modal-birth').textContent;
  document.getElementById('update-phone').value = document.getElementById('modal-phone').textContent;
  document.getElementById('update-address').value = document.getElementById('modal-address').textContent;

  modalMore.hide();
  modalUpdate.show();
});

// Bấm Back → quay lại modal1
document.getElementById('btnBack').addEventListener('click', function() {
  modalUpdate.hide();
  modalMore.show(); // dữ liệu modal1 giữ nguyên
});

// Bấm Save Changes → cập nhật modal1
document.getElementById('btnSave').addEventListener('click', function() {
  const name = document.getElementById('update-name').value;
  const email = document.getElementById('update-email').value;
  const birth = document.getElementById('update-birth').value;
  const phone = document.getElementById('update-phone').value;
  const address = document.getElementById('update-address').value;

  // Cập nhật modal1
  document.getElementById('modal-name').textContent = name;
  document.getElementById('modal-email').textContent = email;
  document.getElementById('modal-birth').textContent = birth;
  document.getElementById('modal-phone').textContent = phone;
  document.getElementById('modal-address').textContent = address;

  modalUpdate.hide();
  modalMore.show();

  // Thêm nút Save vào modal1 nếu chưa có
  if (!document.getElementById('btnSaveModal1')) {
    const saveBtn = document.createElement('button');
    saveBtn.id = 'btnSaveModal1';
    saveBtn.className = 'btn btn-success';
    saveBtn.textContent = 'Save';
    saveBtn.addEventListener('click', function() {
      // Xử lý lưu dữ liệu lên server hoặc AJAX
      alert('Data is saved successfully!');
      // Sau khi lưu xong → đóng modal1
      modalMore.hide();
      // Sau khi lưu xong, có thể xóa nút nếu muốn
      saveBtn.remove();
    });
    modalMoreFooter.appendChild(saveBtn);
  }
});

// Modal confirm
const modalDeleteEl = document.getElementById('modalDeleteConfirm');
const modalDelete = new bootstrap.Modal(modalDeleteEl);

// Khi bấm Delete trong modal More
document.getElementById('btnDelete').addEventListener('click', function () {
  modalMore.hide();
  modalDelete.show();
});

// Khi bấm Delete Confirm
document.getElementById('btnDeleteConfirm').addEventListener('click', function () {
  const id = document.getElementById('modal-id').textContent;

  fetch(`/students/delete/${id}`, {
    method: "POST"
  })
    .then(res => {
      if (res.ok) {
        // Xoá thành công → reload trang
        window.location.reload();
      } else {
        alert("Failed to delete student");
      }
    });
});


